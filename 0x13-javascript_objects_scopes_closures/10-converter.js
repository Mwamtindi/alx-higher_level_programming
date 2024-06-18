#!/usr/bin/node

exports.converter = function (base) {
  function NumConverter (b) {
    return b.toString(base);
  }

  return NumConverter;
};
