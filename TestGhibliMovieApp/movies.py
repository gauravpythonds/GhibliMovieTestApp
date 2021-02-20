#!/usr/bin/env python
import os
import requests
import copy
from requests.exceptions import RequestException

import people as peo


def fetchMovies():
    """
    :author: Gaurav Singh
    :return: movie list
    :decription: fetch list of movies from api
    """
    movies_list = None
    api_endpoint_films = "https://ghibliapi.herokuapp.com/films"
    try:
        response = requests.get(api_endpoint_films)
        print(f"Endpoint /films Response Status code is: {response}")
        response.raise_for_status()
    except requests.exceptions.RequestException as exception:
        print(f"Exception is: {exception}")
        raise SystemExit(exception)
    else:
        movies_list = response.json()
    return movies_list


def people_field(movies_list, people_list):
    """
    :author: Gaurav Singh
    :param movies_list: movie list
    :param all_people: people list
    :return: people data for respective movie
    :decription: fields people for movie
    """
    movies_with_people = copy.deepcopy(movies_list)
    people_id_map = peo.filmPeopleID(people_list)
    for x in movies_with_people:
        x["people"] = people_id_map.get(x["id"], [])
    return movies_with_people
