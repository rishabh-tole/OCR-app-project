const _fetch = require('node-fetch');
const _cheerio = require('cheerio');
const _htmlparser = require('htmlparser2');
const { Promise } = require('bluebird');

_fetch.promise = Promise;

async function scrapeWebPage(url) {
  const response = await _fetch(url);
  const body = await response.text();

  const dom = _htmlparser.parseDOM(body);
  const $ = _cheerio.load(dom);

  const statsElements = $("div.trn-site__container .trn-profile .trn-scont .trn-scont__content .trn-card .r6-season-list .r6-season .r6-season__stats .trn-defstats").children('.trn-defstat');

  for(let index = 0; index<statsElements.length; index++) {
    let nameElement = $('.trn-defstat__name', statsElements[index]);

    let statElement = $('.trn-defstat__value', statsElements[index]);
    console.log(nameElement.text().trim(), statElement.text().trim());
    console.log('----');
  }
  const stats = [];
  
  return stats;
}


async function main(name) {
   const stats = await scrapeWebPage('https://r6.tracker.network/profile/xbox/'+ name);
   console.log(name)
   console.log("---------------------------")
   console

}

main("xxheadshotxx890")
