/**
 * Encodes a URL to a shortened URL.
 *
 * @param {string} longUrl
 * @return {string}
 */

var encodeDic = {};
var decodeDic = {};
var base = "http://tinyurl.com/";

var encode = function (longUrl) {
  let shortUrl = this.base + Math.random().toString(36).substr(2, 7);
  encodeDic[longUrl] = shortUrl;
  decodeDic[shortUrl] = longUrl;
  return shortUrl;
};

/**
 * Decodes a shortened URL to its original URL.
 *
 * @param {string} shortUrl
 * @return {string}
 */
var decode = function (shortUrl) {
  return decodeDic[shortUrl];
};

/**
 * Your functions will be called as such:
 * decode(encode(url));
 */
