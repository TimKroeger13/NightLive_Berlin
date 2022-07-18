import psycopg2
import random
from datetime import datetime
import json
from flask import Flask, request, redirect, url_for, render_template, jsonify, after_this_request
