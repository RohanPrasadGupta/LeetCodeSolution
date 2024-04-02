/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function (emails) {
  let eSet = new Set();

  for (let email of emails) {
    let [local, domain] = email.split("@");

    let pIndex = local.indexOf("+");
    if (pIndex !== -1) {
      local = local.substring(0, pIndex);
    }

    local = local.replace(/\./g, "");
    final = local + "@" + domain;
    eSet.add(final);
  }
  return eSet.size;
};
