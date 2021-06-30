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