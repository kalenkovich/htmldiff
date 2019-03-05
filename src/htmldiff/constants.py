"""Constants."""
import re

COMMENT_RE = re.compile(b'<!--.*?-->', re.S)
# Do not process script or style tags
TAG_RE = re.compile(b'(^(?!<script$)|^(?!<style$)).*?>.*?</script>|<.*?>', re.S)
HEAD_RE = re.compile(b'<\s*head\s*>', re.S | re.I)
WS_RE = re.compile(b'^([ \n\r\t]|&nbsp;)+$')
WORD_RE = re.compile(
    b'([^ \n\r\t,.&;/#=<>()-]+|(?:[ \n\r\t]|&nbsp;)+|[,.&;/#=<>()-])'
)
ID_HREF_REPLACE = re.compile(b' (id|href)=\"[#A-Za-z_]+?[#\w\-\:\.].*?\"')

STOPWORDS = (
    'a',
    'about',
    'an',
    'and',
    'are',
    'as',
    'at',
    'be',
    'by',
    'for',
    'from',
    'have',
    'how',
    'I',
    'in',
    'is',
    'it',
    'of',
    'on',
    'or',
    'that',
    'the',
    'this',
    'to',
    'was',
    'what',
    'when',
    'where',
    'who',
    'will',
    'with',
)
