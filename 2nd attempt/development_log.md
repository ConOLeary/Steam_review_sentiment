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