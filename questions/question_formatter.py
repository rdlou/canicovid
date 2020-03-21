from nltk.stem import PorterStemmer
import string

translator = str.maketrans('', '', string.punctuation)
ps = PorterStemmer() 

def formatter(question):
    response = []
    searchable = sorted(str(question).lower().translate(translator).split())
    stopwords = {"ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"}
    searchable_response = []
    for s in searchable:
        response.append(s)
        if s in stopwords:
            continue
        stem  = str(ps.stem(s))
        ion = stem + "ion"
        ing = stem + "ing"
        _or = stem + "or"
        response.append(stem)
        response.append(ion)
        response.append(ing)
        response.append(_or)
    return " ".join(set(response))