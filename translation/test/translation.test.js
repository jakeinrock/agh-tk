import {expect} from 'chai';

import {getTranslations} from "../translation.js";

describe('Should get translations', function() {

    it('should get english translations', function() {
        return getTranslations('dzwony', ['en'])
            .then(function(translated){
                expect(translated).deep.to.equal(['bells']);
            });
    })

    it('should get english and german translations', function() {
        return getTranslations('dzwony', ['de', 'en'])
            .then(function(translated){
                expect(translated).deep.to.equal(['Glocken', 'bells']);
            });
    })


});
