from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def match_cv_to_job(cv_text: str, job_summary: str):
    stop_words = set(stopwords.words('english'))
    cv_words = [word.lower() for word in word_tokenize(cv_text) if word.isalpha() and word not in stop_words]
    job_words = [word.lower() for word in word_tokenize(job_summary) if word.isalpha() and word not in stop_words]

    cv_freq = FreqDist(cv_words)
    job_freq = FreqDist(job_words)

    # Calculate match score
    match_score = sum(min(cv_freq[word], job_freq.get(word, 0)) for word in job_words)
    return match_score
