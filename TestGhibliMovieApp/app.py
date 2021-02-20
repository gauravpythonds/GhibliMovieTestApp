#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from flask import jsonify
from flask import Flask, render_template
from flask_caching import Cache

import movies as mov
import people as pep


def main():
    FLASK_DEBUG = False
    app = create_app()
    app.run(port=8000, debug=FLASK_DEBUG, threaded=True)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    config = {'DEBUG': True}
    app.config.from_mapping(config)
    cache = Cache(app, config={'CACHE_TYPE': 'simple',
                  'CACHE_DEFAULT_TIMEOUT': 60})

    @app.route('/movies/', methods=['GET'])
    @cache.cached(timeout=60)
    def fetchMoviesWithPeople():
        '''
        :author: Gaurav Singh
        :description: This definition is used to final movies list with people
        appeared in those movies
        :return: movie list from Ghibli's film API
        '''

        movies = mov.fetchMovies()
        if movies is None:
            return 'Not able to retrieve  movies from Ghibli Api'
        people_movie = pep.fetchPeople()
        if people_movie is None:
            return 'Not able to retrieve people for movies from Ghibli Api'
        movie_list = mov.people_field(movies, people_movie)
        return render_template('ghiblimovies.html', films=movie_list)

    return app


if __name__ == '__main__':
    main()
