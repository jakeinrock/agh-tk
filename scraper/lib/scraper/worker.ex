defmodule Scraper.Worker do
  require Logger

  alias Scraper.Sender
  alias Scraper.FormatParser

  def run(%{path: path, file_types: file_types} = args) do
    Logger.info("Traversing started for #{path}")

    Path.wildcard(path)
    |> Enum.filter(&filter(&1, file_types))
    |> Enum.each(&parse_and_send(&1, args))
  end

  defp filter(_path, []), do: true

  defp filter(path, list) do
    format = Path.extname(path)
    Enum.member?(list, format)
  end

  defp parse_and_send(path, %{json: json} = args) do
      Path.extname(path)
      |> FormatParser.get_key()
      |> Enum.each(&send(path, args, &1))
  end

  defp send(path, %{json: json}, key) do
    Map.put(json, "file", path)
    |> Map.put("routingKey", key)
    |> Sender.send(key)
  end
end
