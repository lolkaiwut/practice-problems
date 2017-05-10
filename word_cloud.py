def word_cloud(str):
    word_cloud_dict = {}
    for word in str.split():
    	word_cloud_dict[word] = str.count(word)
    return word_cloud_dict
print word_cloud('After beating the eggs, Dana read the next step:')
print word_cloud('Add milk and eggs, then add flour and sugar.')
print word_cloud('seventy-one sixty-four')
#print word_cloud('We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake.')
print word_cloud('The bill came to five dollars.')
