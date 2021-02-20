#!/usr/bin/env python
import os
import requests
import copy

from requests.exceptions import RequestException


def fetchPeople():
    """
    :author: Gaurav Singh
    :description: fetch people details for each movie
    :return: people data
    """
    people = None
    api_endpoint_people = "https://ghibliapi.herokuapp.com/people"

    try:
        response = requests.get(api_endpoint_people)
        print(f"Endpoint /people Response Status code is: {response}")
        response.raise_for_status()
    except requests.exceptions.RequestException as exception:
        print(f"Exception is: {exception}")
        raise SystemExit(exception)
    else:
        people = response.json()

    return people


def build_dict_id_people(people):
    """
    :author: Gaurav Singh
    :param people: people
    :return: return peopleid dictionary
    :decription: This method is just to build and return peopleid dictionary
    """

    peopleid = {}
    for p in people:
        if "films" in p:
            for id in p["films"]:
                if id in peopleid:
                    peopleid[id].append(p["name"])
                else:
                    peopleid[id] = [p["name"]]
    return peopleid


def filmPeopleID(people_list):
    """
    :author: Gaurav Singh
    :param people: people
    :return: return mapped film id for people
    :description: This method is just to map people id for each movie
    and return film people id
    """
    people = copy.deepcopy(people_list)

    for p in people:
        if "films" in p:
            p["films"] = list(map(lambda x: x.split("/")[-1], p["films"]))
    filmpeopleid = build_dict_id_people(people)
    return filmpeopleid
