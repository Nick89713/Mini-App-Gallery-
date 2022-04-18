from tkinter import *
import getpass
from tkinter import ttk
import psycopg2
import pandas as pd
from PIL import ImageTk,Image


def DB_info():                              #simple return function
    user = 'postgres'
    password = 'abcd2448'
    db_name = "miniGallery"

    return user,password,db_name
