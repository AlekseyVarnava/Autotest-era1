from dataclasses import dataclass


@dataclass
class Person:
    tel_number: str = None
    one_name: str = None
    two_name: str = None
    three_name: str = None
    email_me: str = None
    series_number: int = None
    my_city: str = None
    day_13years: str = None
    day_18years: str = None
    series_study: int = None
    ogrn_number: int = None
    job_rol: str = None
    day_start_job: int = None
    day_finish_job: int = None
