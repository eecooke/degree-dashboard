import pandas as pd
import numpy as np
import math as m

mathcodes = ['MATH', 'CS', 'CO', 'STAT', 'AMATH', 'PMATH']
coopcodes = ['COOP', 'PD', 'WKRPT']

# Requirements come from UWaterloo Calendar Year 2014-2015
# Course units have been converted to number (#) of courses
def reqs(df):
    # General requirements for math students
    everything = pd.DataFrame({'min': [40, 0, 0, 8, 60], 'max': [50, 8, 5, 100, 100]},
                              index = ['TOTAL', 'FAILED', 'UNUSABLE', 'TERMS', 'CAV'])
    # Requirements for my program: Mathematical Studies major, Computer Science minor, coop program
    math = pd.DataFrame({'min': [26, 10, 10, 60], 'max': [50, 50, 50, 100]},
                        index = ['MATHS', 'UPPER MATHS', 'NON MATHS', 'MAV'])
    cs = pd.DataFrame({'min': [8, 6, 0, 60], 'max': [50, 50, 2, 100]},
                       index = ['CS', 'UPPER CS', 'FAILED CS', 'CSAV'])
    coop = pd.DataFrame({'min': [5, 5, 4], 'max': [6, 6, 5]},
                         index = ['COOP', 'PD', 'WKRPT'])
        
    dfc = df.replace('WD', np.nan).replace('CR', 1).replace('NCR', 0)
    
    # Dataframe that does not include courses that were taken twice
    nodup = dfc.drop_duplicates(subset=['faculty', 'code']);
    
    # Dataframe that does not include coop courses
    nocoop = dfc[dfc['faculty'].map(lambda x : x not in ["COOP", "PD", "WKRPT"])]
    
    # Add columns to each dataframe that provide the statistics based on transcript
    math['actual'] = math_stats(nodup)
    coop['actual'] = coop_stats(nodup)
    cs['actual'] = cs_stats(nodup)
    
    # TODO: Be a little more precise.
    # a) Check definition of unusable courses. Confirm units
    # b) Figure out how to count number of terms. Also, max number of terms?
    # c) Include exactly the courses that UW includes in averages
    actual = []
    actual.append(nocoop.shape[0])
    actual.append(nocoop[nocoop['grade'] < 50].shape[0])
    actual.append(nocoop[nocoop['grade'].map(lambda x : x < 50 or m.isnan(x))].shape[0])
    actual.append(6)
    actual.append(nocoop['grade'].mean())
    everything['actual'] = actual
    
    everything = everything.append([math, coop, cs])
    # Negative requirements do not make sense
    everything['need'] = (everything['min'] - everything['actual']).map(lambda x : max([x,0]))
    
    return everything.applymap(lambda x : round(x,2))
    
# Returns list of statistics relating to Mathematical Studies major
def math_stats(df):    
    dfc = df[df['faculty'].map(lambda x : x in mathcodes)]
    
    actual = []
    actual.append(dfc.shape[0])    
    # Upper Math courses refer to 300 or higher level courses
    actual.append(dfc[dfc['code'] >= '300'].shape[0])
    # Non math courses exclude courses crosslisted as math courses
    actual.append(df[df['faculty'].map(lambda x : x not in mathcodes)].shape[0])
    actual.append(dfc['grade'].mean())
    
    return actual
   
# Returns list of statistics relating to Computer Science minor
def cs_stats(df):    
    dfc = df[df['faculty'] == "CS"]
    
    actual = []
    actual.append(dfc.shape[0])
    # Upper CS courses refer to 200 or higher level courses
    actual.append(dfc[dfc['code'] >= '200'].shape[0])
    actual.append(dfc[dfc['grade'] < 50].shape[0])
    actual.append(dfc['grade'].mean())
    
    return actual
    
# Returns lists of statistics relating to coop specific requirements
def coop_stats(df):    
    dfc = df[df['grade'] > 0]
    
    counts = pd.value_counts(dfc['faculty'].values)    
    # Include PD 2 work report in count
    if ('2' in dfc[dfc['faculty'] == 'PD'].values):
        counts['WKRPT'] += 1
    
    return counts[coopcodes]

# Must complete one from EVERY following list
# https://ugradcalendar.uwaterloo.ca/page/MATH-Degree-Requirements-for-Math-students
# https://ugradcalendar.uwaterloo.ca/page/MATH-Mathematical-Studies
math_studies_core = {
    "MATH": [
        ["127", "137", "147"], # Calculus 1
        ["128", "138", "148"], # Calculus 2
        ["135", "145"],        # Algebra
        ["106", "136", "146"], # Linear Algebra 1
        ["225", "235", "245"], # Linear Algebra 2
        ["207", "237", "247",  # Calculus 3
         "229", "239", "249"]  # Combinatorics
    ], "STAT": [
        ["220", "230", "240"], # Probability
        ["221", "231", "241"]  # Statistics
    ], "CS": [
        ["115", "135", "145"], # Functional Programming
        ["116", "136", "146"]  # Algo Design and Data Abstraction
    ]
}

# Must complete one from EVERY following list
# https://ugradcalendar.uwaterloo.ca/page/MATH-Computer-Science-Minor-1
cs_minor = {
    "MATH": [
        ["103", "106", "114", "115", "136", "146"], # Linear Algebra
        ["104", "116", "117", "127", "137", "147"]  # Calculus
    ], "CS": [
        ["115", "135", "145"], # Functional Programming
        ["116", "136", "146"], # Algo Design and Data Abstraction
        ["230", "234", "246"], 
        ["230", "234", "246"]
    ]
}

co_upper = ["430", "434", "439", "440", "442", "444", "446", "450", "452", "453", \
            "454", "456", "459", "463", "466", "471", "481", "485", "487"]
# Must complete one from EVERY following list
# https://ugradcalendar.uwaterloo.ca/page/MATH-Combinatorics-and-Optimization-Minor
co_minor = {
    "MATH": [
        ["103", "106", "114", "115", "136", "146"], # Linear Algebra
        ["104", "116", "117", "127", "137", "147"], # Calculus
        ["135", "145"], # ECE 103, PMATH 340        # Discrete Math
        ["239", "249"]  # Combinatorics
    ], "CO": [
        ["250", "255"], # Optimization
        # Represents three 
        ["330", "331", "342", "351", "353", "367", "370", "372"].extend(co_upper),
        ["330", "331", "342", "351", "353", "367", "370", "372"].extend(co_upper),
        ["330", "331", "342", "351", "353", "367", "370", "372"].extend(co_upper)
    ]
}
    
# Must complete one of ANY following lists
eng_skills = {
    "ENGL": [
        ["109", "129R", "140R"] 
    ], "ESL": [
        ["129R", "101R", "102R"]
    ], "SPCOM": [
        ["100", "111", "223"]
    ]
}