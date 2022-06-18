import translate from "translate-google";

export function getTranslations(phrase, languages){
    return Promise.all(languages.map(lang => translate(phrase, { from: 'pl', to: lang })))
}