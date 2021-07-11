11 / 7 / 2021

> MIN_ENGLISH at 0.0 still cancels out non-english ¯\_(ツ)_/¯

7 / 7 / 2021

> https://radimrehurek.com/gensim/models/word2vec.html
  https://rare-technologies.com/word2vec-tutorial/
> Language filtering seems to have no effect on efficacy of og model; have incorportated into new, embedded approach incase it has some use in that instance. Same goes to word type filtering, although I suspect that could be relevant to this newest approach.

6 / 7 / 2021

> https://www.youtube.com/watch?v=wNBaNhvL4pg
  https://www.youtube.com/watch?v=gQddtTdmG_8
  https://towardsdatascience.com/word-embeddings-exploration-explanation-and-exploitation-with-code-in-python-5dac99d5d795
  https://stackoverflow.com/questions/57599259/sklearngensim-how-to-use-gensims-word2vec-embedding-for-sklearn-text-classifi

4 / 7 / 2021

> At the smaller volums of input data I use while experimenting, the model's results are quite ireegular, so I have increased the k in f_fold to 20
> With k_folds = 5 (and input rows = 300) => overall accuracy ~= 0.65, 0.65, 0.63, 0.59, 0.58
> With k_folds = 20(and input rows = 300) => overall accuracy ~= 0.61. I think I may be overfolding for the amoutn of data (300 rows) as many of the confusion matrixes for the folds are extremely divient in their results so i'm not sure if this would yield less variance between runs.
> With k_folds = 20(and input rows = 500, features = 500) => overall accuracy ~= 0.70, 0.64, 0.68, 0.69. Variance is down which is nice, but more interesting is that accuracy is up.
> With k_folds = 20(and input rows = 1000, features = 500) => overall accuracy ~= 0.68, 0.60
> With k_folds = 20(and input rows = 500, features = 500) => overall accuracy ~= 0.65
> With k_folds = 20(and input rows = 500, features = 1000) => overall accuracy ~= 0.64, 0.58
> With k_folds = 20(and input rows = 500, features = 200) => overall accuracy ~= 0.57, 0.76, 0.49, 0.65 0.56. Load times are mad fast but variance is mad high .. interesting. Average accuracy is still lower then with features = 500.
> I am wondering now whether having set activation="rely" in the MLP classifier is stopping inputs from having negative weighting

2 / 7 / 2021

> "In Python, our objects, and arrays are called dictionaries and lists respectively" https://oppor.com/shuffling-data-json/
        Useful for future reference. Found this when looking into how json file of learning data could be shuffled. Perhaps I could access the data randomly rather than randomising the order of the data. I am worried though that this former approach could significantly slow down the cell that reads in the learning data.
> Reviews loading in randomised order. When printed, the polarities still seem to clump up by True and False.. Needs further investigation. English language filtering being moved from data reading cell to filtering cell - might give each type of filtering their own cell actually
> Getting roughly the same results for 3,000 rows as I do for 200 - which should speed up my trial and error cycle
> Got rid of my data 'thickening' and accuracy dropped 10% .. either I was onto something or my new code is screwed up

1 / 7 / 2021

> Filter cell now returns reviews as list of strings rather than list of lists. This seems to have dealt with type issues when playing the cells in a non-linear sequence, which was caused by reviews entering the filter cell as one type and leaving as another.
> Tags seem to be being assigned per word - this needs investigation
> input rows = 1500, MAX_FEATURES = 500, ACCEPTABLE_TAGS = ALL_TAGS.
    Overall accuracy ~= 0.70
> Same as above but with ACCEPTABLE_TAGS= ['FW', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS',
 'POS', 'RB', 'RBR', 'RBS', 'RP', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WP$']
    Overall accuracy ~= 0.72 -.-
> Same as above but with MAX_FEATURES = 1500 => Overall accuracy ~= 0.71
> Would be handy if I could find a way to shuffle the json file entries, as for some reason there's a huge swath of positive-only reviews at the start that mean a large number of entries have to be read to get an unbiased sampl
> For some reason lemmatizing words reduces the accuracy by ~= 0.03
> Probably my idea of 'thickening' the data is inane as the modal learns from the training data as much as it can, regardless of whether i've 'thickened' it first by interwieving duplicates of the training data into the training data

30 / 6 / 2021

> Nueral net should actually be nearly off words now instead of letters. Hopefully this means if I start filtering out certain word types again that this time that will actually have tangiable bearing on the accuracy

29 / 6 / 2021

> After a hiatus, it is apparent to me that the approach I took to 'thicken' the training data is infact a 'cheat' because the thickened training data includes testing data.
> Perhaps sorting word frequencies by their volume is screwing up the nueral net
> Seemingly it turns out that when I was choosing frequent words as features I had been looking at letters and not words

17 / 6 / 2021

> The first load of reviews all being positive is indeed just the nature of the data
> way I implemented k-fold is a mircale .. for some reason
> 'jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10' if there's an issue with data rates
> excluding certain word types knocks my model down ~0.1 in overall accuracy
> cahnging MAX_FEATURES from 200 to 500 sees a marginal increase in accuracy of 0.01

15 / 6 / 2021

> Going to play with layer of MLP model
> 0.6719 with hidden_layer_sizes=(256,128,64,32)
> Accuracy with ACCEPTABLE_TAGS = ['CC', 'DT', 'EX', 'FW', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'PDT',
 'POS', 'PRP', 'PRP$', 'RP', 'TO', 'UH', 'VBD', 'VBG', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB'] is 0.825.
 With ACCEPTABLE_TAGS = ALL_TAGS is 0.84. So apparently my word filtering is redundant


14 / 6 / 2021

> trying to label confusion matrix so it doesn't confuse me
> perhaps accuracy of existing approach scales with whether the analysed reviews are overwhelmingly positive/negative
> overall accuracy:  0.6507936507936508 when Trues: 170 Falses: 208