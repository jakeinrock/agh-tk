﻿using System;
using System.Text;
using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Presentation;
using DocumentFormat.OpenXml.Spreadsheet;
using DocumentFormat.OpenXml.Wordprocessing;

public class MicrosoftExtractor
{
    public string ReadMessageFromExcel(Stream fileStream)
    {
        using (SpreadsheetDocument spreadsheetDocument = SpreadsheetDocument.Open(fileStream, false))
        {
            StringBuilder text = new StringBuilder();

            WorkbookPart workbookPart = spreadsheetDocument.WorkbookPart;
            SharedStringTablePart sstpart = workbookPart.GetPartsOfType<SharedStringTablePart>().First();
            SharedStringTable sst = sstpart.SharedStringTable;

            WorksheetPart worksheetPart = workbookPart.WorksheetParts.First();
            Worksheet sheet = worksheetPart.Worksheet;

            var rows = sheet.Descendants<Row>();

            foreach (Row row in rows)
            {
                foreach (Cell c in row.Elements<Cell>())
                {
                    if ((c.DataType != null) && (c.DataType == CellValues.SharedString))
                    {
                        int ssid = int.Parse(c.CellValue.Text);
                        string str = sst.ChildElements[ssid].InnerText;
                        text.Append(str);
                        text.Append(Environment.NewLine);
                    }
                }
            }

            return text.ToString();
        }
    }

    public string ReadMessageFromWord(Stream fileStream)
    {
        string text;

        using (WordprocessingDocument wordDoc = WordprocessingDocument.Open(fileStream, false))
        {
            Body body = wordDoc.MainDocumentPart.Document.Body;
            text = body.InnerText;
            return text;
        }
    }

    public string ReadMessageFromPowerPoint(Stream fileStream)
    {
        Console.WriteLine(fileStream);
        string text = null;

        int numberOfSlides = CountSlides(fileStream);
        for (int i = 0; i < numberOfSlides; i++)
        {
            string newText = GetSlideIdAndText(fileStream, i);
            text += newText;
        }

        return text;
    }


    public static int CountSlides(Stream fileStream)
    {
        using (PresentationDocument presentationDocument = PresentationDocument.Open(fileStream, false))
        {
            if (presentationDocument == null)
            {
                throw new ArgumentNullException("presentationDocument");
            }

            int slidesCount = 0;

            PresentationPart presentationPart = presentationDocument.PresentationPart;
            if (presentationPart != null)
            {
                slidesCount = presentationPart.SlideParts.Count();
            }

            return slidesCount;
        }
    }

    public static string GetSlideIdAndText(Stream fileStream, int index)
    {
        using (PresentationDocument ppt = PresentationDocument.Open(fileStream, false))
        {
            PresentationPart part = ppt.PresentationPart;
            OpenXmlElementList slideIds = part.Presentation.SlideIdList.ChildElements;

            string relId = (slideIds[index] as SlideId).RelationshipId;

            SlidePart slide = (SlidePart) part.GetPartById(relId);

            StringBuilder paragraphText = new StringBuilder();

            IEnumerable<DocumentFormat.OpenXml.Drawing.Text> texts =
                slide.Slide.Descendants<DocumentFormat.OpenXml.Drawing.Text>();
            foreach (DocumentFormat.OpenXml.Drawing.Text text in texts)
            {
                paragraphText.Append(text.Text);
            }

            return paragraphText.ToString();
        }
    }
}