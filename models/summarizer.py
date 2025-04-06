import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def summarize_job_description(job_desc: str):
    sentences = sent_tokenize(job_desc)
    words = word_tokenize(job_desc.lower())

    # Remove stopwords and non-alphabetic words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

    # Frequency distribution of words
    freq_dist = FreqDist(filtered_words)

    # Rank sentences based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        score = sum(freq_dist[word] for word in sentence_words if word in freq_dist)
        sentence_scores[sentence] = score

    # Sort sentences by score and get top 3
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(sorted_sentences[:3])

    return summary
