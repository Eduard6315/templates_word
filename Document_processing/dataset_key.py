from settings import template_heading_2, template_heading_1, template_body_1, template_body_2, template_bottom_1, \
    template_bottom_2
import datetime

current_datetime = datetime.datetime.now()


date_dict = {
    "day_month": current_datetime.day,
    "month": current_datetime.strftime("%B"),
    "year": current_datetime.year
}


dataset = {
    template_heading_1: {"company": "Иокогава Электрик СНГ", "project": "YRU-C133045"},
    template_heading_2: {"number": "12"},
    template_body_1: {"company_name": "Иокогава Электрик СНГ",
                      "company_adress": "129110, г. Москва, Самарская ул., д.1", "court_name": "города Москвы",
                      "date_from": "30_03_2024", "case_number": "215",
                      "financial_organization": "YRU_Yokogawa", "orgn": "NAICS", "inn": "1239843489",
                      "reg_adress": "129110, г. Москва, Самарская ул., д.1"},
    template_body_2: {
        "bill_number": "12345",
        "company_name": "Иокогава Электрик СНГ",
        "rows": [
            {
                "pp_number": 1,
                "lot_number": 5,
                "pp_date": "20/02/2024",
                "winer_name": "Djon",
                "payment_purpose": "payment",
                "payment_sum": 150000
            },
            {
                "pp_number": 2,
                "lot_number": 6,
                "pp_date": "27/01/2024",
                "winer_name": "Нelen",
                "payment_purpose": "payment",
                "payment_sum": 110000
            },
            {
                "pp_number": 3,
                "lot_number": 24,
                "pp_date": "01/02/2023",
                "winer_name": "Mike",
                "payment_purpose": "payment",
                "payment_sum": 100000
            },

        ]
    },
    template_bottom_1 : {
        "sign": "Ваша подпись",
        "day": str(date_dict["day_month"]),
        "month": date_dict["month"],
          "year": str(date_dict["year"])[-2:]
    },
    template_bottom_2 : {
            "full_name": "Сафонов Эдуард Олегович",
            "credentials": "ACCD",

        }


}
