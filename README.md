# What's in [an embedding]?
## Bloomberg Industry Group 2022 Datathon Challenge 

## What is an embedding?
An embedding is a dense mathematical representation of some input data.  For this challenge, the embedding is the first half of Bloomberg INDG's prototype model to assign news articles to various publishing channels.  The output is a compressed representation of the input text fed to the model.

## The Data
There are two datasets for this challenge

- `cnn_samples.csv` - A small sample of CNN articles from the `cnn_dailymail` [dataset](https://huggingface.co/datasets/cnn_dailymail) along with generated embeddings.  The data is made available under the [Apache-2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
- `federal_samples.csv` - A sample of press releases from various US government agencies along with embeddings.  

## The Challenge 

### Part One (50 points possible)
There are five mystery articles with embedding shown in `mystery_challenge.csv`.  For each article, make your best educated guess as to what the mystery article is about.  It can be as broad or as precise as you'd like.  (Feel free to offer up a phrase, sentence, or even a paragraph to describe your guess.  Dissertations not welcome.)

The closest team for each article gets 10 points, the 2nd closest team gets 5 points, the 3rd closest gets 2 points.

### Part Two (30 points possible)

Build a binary classifier using the embeddings!  Go crazy and use the model for something it's not intended for.

### Bonus (Mystery prize to be sent after the event)

Guess the 6th mystery embedding.  

*Hint: It's not a news article.*

## Now what?

You can do lots of things with embeddings but mostly, they are inputs for other models.  Theoretically, similar input data will generate similar embeddings.  Though you should probably check for yourself if this is true.

There are numerous ways to measure similarity.  The most common methods are euclidian distance and cosine similarity but don't let yourself be constrained to these.  If you have a good hypothesis for a novel similarity measure, here's your chance to test it out!

Once you decide on a distance metric, you can use methods like k-Nearest Neighbors to compare data points to groups of neighbors.  You can even use graphs to represent relationships between data points.  Here's your chance to experiment and go wild!

## I need more data points
You'll probably need more data.  Here's where you can use our API to get more embeddings.  Each time will be provided an API key which will be throttled to X number of calls per minute.

### Via Code 
*Insert instructions here* 
See sample code.

### Via Postman


## FAQs
### How do I win?
Get the most points as a team 

### That's a lot of numbers, do I need to use all of them?
Nope.  Regularization is an important technique in statistics and data science.

### What's the mystery prize?
I haven't figured it out yet.  