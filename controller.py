import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models


def db_cursor():
    return mysql.connect(host=DB_HOST,
                         user=DB_USER,
                         passwd=DB_PASSWD,
                         db=DB_NAME).cursor()


def get_earthquake():
    with db_cursor() as cs:
        cs.execute("""
            SELECT center, magnitude
            FROM earthquake
        """)
        result = [models.EarthquakeBasic(*row) for row in cs.fetchall()]
        return result


def get_earthquake_details(province):
    pro = '%' + province + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT  center, magnitude, date, lat, lon, depth, phrase
            FROM earthquake
            WHERE center like %s
        """, [pro])
        result = [models.EarthquakeDetail(*row) for row in cs.fetchall()]
        return result


def get_average_magnitude_and_phrase(province):
    pro = '%' + province + '%'
    with db_cursor() as cs:
        cs.execute("""
            SET @TestVariable := 'จ.'+ %s;
            SELECT @TestVariable AS province, ROUND(AVG(magnitude),2) average_magnitude, ROUND(AVG(phrase),2) average_phrase
            FROM(
            SELECT  center, magnitude, date, lat, lon, depth, phrase
            FROM earthquake
            WHERE center like %s) eq
        """, [province, pro])
        result = cs.fetchone()
        if result:
            return models.EarthquakeAverage(*result)
        else:
            abort(404)

# def get_province_numbers_of_earthquakes(province):
#     pro = '%' + province + '%'
#     with db_cursor() as cs:
#         cs.execute("""
#             SET @TestVariable := 'จ.'+ %s;
#             SELECT province, COUNT(*) as number_of_earthquake
#             FROM
#             (SELECT  @TestVariable AS province, magnitude, date, lat, lon, depth, phrase
#             FROM earthquake 
#             WHERE center like %s) pro_eq
#         """, [province, pro])    
#     return


def get_landslide():
    with db_cursor() as cs:
        cs.execute("""
            SELECT province, `risk-landslide-area`
            FROM landslide
        """)
        result = [models.LandslideBasic(*row) for row in cs.fetchall()]
        return result


def get_landslide_details(province):
    pro = '%' + province + '%'
    with db_cursor() as cs:
        cs.execute("""
                SELECT  province, district, `sub-district`, `risk-landslide-village`, `risk-landslide-area`
                FROM landslide
                WHERE province like %s
            """, [pro])
        result = [models.LandslideDetail(*row) for row in cs.fetchall()]
        return result


def get_landslide_earthquake_ratio():
    list = []
    landslide_province = ['จ.เชียงใหม่', 'จ.ตาก', 'จ.แม่ฮ่องสอน', 'จ.น่าน', 'จ.กาญจนบุรี', 'จ.เชียงราย', 'จ.ลำปาง', 'จ.สุราษฎร์ธานี', 'จ.เลย', 'จ.เพชรบูรณ์', 'จ.อุตรดิตถ์',
                        'จ.แพร่', 'จ.ยะลา', 'จ.เพชรบุรี', 'จ.พิษณุโลก', 'จ.อุทัยธานี', 'จ.ชัยภูมิ', 'จ.นครราชสีมา', 'จ.ประจวบคีรีขันธ์', 'จ.พะเยา', 'จ.นครศรีธรรมราช', 'จ.ชุมพร'
                        'จ.ระนอง', 'จ.พังงา', 'จ.ลำพูน', 'จ.สงขลา', 'จ.นราธิวาส', 'จ.จันทบุรี', 'จ.กำแพงเพชร', 'จ.สุโขทัย', 'จ.ราชบุรี', 'จ.ตรัง', 'จ.ปราจีนบุรี', 'จ.สตูล', 
                        'จ.อุบลราชธานี', 'จ.กระบี่', 'จ.สระแก้ว', 'จ.พัทลุง', 'จ.อุดรธานี', 'จ.ศรีสะเกษ', 'จ.ขอนแก่น', 'จ.นครสวรรค์', 'จ.นครนายก', 'จ.สระบุรี', 'จ.ตราด', 'จ.ระยอง', 
                        'จ.สุพรรณบุรี', 'จ.ชลบุรี', 'จ.ลพบุรี', 'จ.หนองบัวลำภู', 'จ.หนองคาย', 'จ.ภูเก็ต', 'จ.ฉะเชิงเทรา', 'จ.ปัตตานี']
    for i in range(len(landslide_province)):
        pro = '%' + landslide_province[i] + '%'
        with db_cursor() as cs:
            cs.execute("""
                SELECT e.province, COUNT(*) as number_of_earthquake, `risk-landslide-village`
                FROM
                (SELECT  @TestVariable:=%s AS province, magnitude, date, lat, lon, depth, phrase
                FROM earthquake 
                WHERE center like %s) e
                INNER JOIN landslide l
                WHERE e.province = l.province
                GROUP BY e.province, `risk-landslide-village`
            """, [landslide_province[i],pro])  
        result = cs.fetchone()
        if result:
            result_json = {
                "province": result[0],
                "number_of_earthquake": result[1],
                "risk-landslide-village": result[2],
            }
            list.append(result_json)
    return list


def get_landslide_and_earthquake_ratio(province):
    pro = '%' + province + '%'
    with db_cursor() as cs:
        cs.execute("""
            SET @TestVariable := 'จ.'+ %s;
            SELECT e.province, COUNT(*) as number_of_earthquake, `risk-landslide-village`
            FROM
            (SELECT  @TestVariable AS province, magnitude, date, lat, lon, depth, phrase
            FROM earthquake 
            WHERE center like %s) e
            INNER JOIN landslide l
            WHERE e.province = l.province
            GROUP BY e.province, `risk-landslide-village`
        """, [province, pro])


def get_disaster():
    with db_cursor() as cs:
        cs.execute("""
            SELECT month, north, `north-east`, central, east, `south-east`, `south-west`
            FROM disaster

        """)
        result = [models.DisasterBasic(*row) for row in cs.fetchall()]
        return result


def get_disaster_details(month):
    pro = '%' + month + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT  north, `north-east`, central, east, `south-east`, `south-west`
            FROM disaster
            WHERE month like %s
        """, [pro])
        result = [models.DisasterDetail(*row) for row in cs.fetchall()]
        return result
