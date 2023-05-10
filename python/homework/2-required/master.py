# def decode_XKCD_tuple(xkcd_values, k): return sorted(
#     map(decode_value, xkcd_values), reverse=True)[:k]
#
#
# def decode_value(xkcd): return list_of_weights_to_number(
#     xkcd_to_list_of_weights(xkcd))
#
#
# def xkcd_to_list_of_weights(xkcd): return [int(
#     x)for x in xkcd.replace('1', '  1').replace('5', ' 5').split()]
# def list_of_weights_to_number(weigths): return sum(
#     [n if n >= weigths[-i] or i == 0else-n for i, n in enumerate(weigths[::-1])])
#
#
# def _01100010_01100001_01100011_01101001_01100001_01110100_01100101_01101101_01101001_00100000_01101001_01101100_00100000_01100011_01110101_01101100_01101111(): pass
