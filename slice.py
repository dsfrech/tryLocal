#
# Get a Substring with a Slice
#
# [:]         extracts the entire sequence from start to end
# [start:]    specifies from the start offset to the end
# [:end]      from the beginning to the end offset
# [start:end] indicates from the start offset to the end offset minus 1
#                                                    ==================
# [start:end:step] 
#
#   NOTE: start is inclusive, end is exclusive
#
upos    = '          1         2'
position= '01234567890123456789012345'
letters = 'abcdefghijklmnopqrstuvwxyz'
print(upos+'\n'+position+'\n'+letters)
print('[:] ',letters[:])
print('[20: ',letters[:20])
print('[12:15] ',letters[12:15])
print('[-3:] ',letters[-3:])
print('[-6:-2] ',letters[-6:-2])
print('[::7] ',letters[::7])
print('[4:20:3] ',letters[4:20:3])
print('[-1::-1] ',letters[-1::-1])
print('[::-1] ',letters[::-1])
