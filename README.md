# Unsupervised Document Summarization using pre-Trained Sentence Embeddings and Graph Centrality

This repository implements an [online demo](https://auto-summ.herokuapp.com/) of the paper [*Unsupervised Document Summarization using pre-Trained Sentence Embeddings and Graph Centrality*](https://aclanthology.org/2021.sdp-1.14/) published in the Second Scholarly Document Processing Workshop (SDP 2021) at NAACL-HLT 2021.

## Usage

### Starting the server

This project is based on the [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework. Detailed explanations about how to use Flask and the configuration files of this project can be found in the excellent [Mega Flask tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). To start the server, you just need to run the following command in the root folder of this project:

    flask run

### Using as a library

Assuming you have your whole document in a single string, using

    from auto_summ.engine import core
    
    centralities = core.algorithm(text)
    
will parse it into sentences, compute the centrality of each one of them according to the algorithm described in the paper and give you back a Pandas dataframe with the following columns:

  * **sentence**, which contains the sentences found in your document.
  * **centrality**, which contains the relevance score (essentially the degree centrality) of each one of the sentences.

## Features

  * A detailed sentence tokenization process based on regular expressions than can accurately handle most cases found in scientific literature.
  * As opposed to the implementation of the paper, this online implementation runs on TF-IDF embeddings for the sake of speed and efficiency. You can easily change this to any of the pre-trained language models found in https://www.sbert.net/.

## Installation

    git clone https://github.com/jarobyte91/auto_summ.git
    cd auto_summ
    pip install -r requirements.txt

## Support

Feel free to send an email to jarobyte91@gmail.com or contact me through any of my social media.

## Contribute

Feel free to use the Issue Tracker or Pull Requests of this repository.

## License

This project is licensed under the MIT License.
