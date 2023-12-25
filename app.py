from flask import Flask
from flask_restful import reqparse, Resource, Api
import sqlite3

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True)
parser.add_argument("time", type=float, required=True)

class Rank(Resource):
    def get(self, checkpoint):
        conn = sqlite3.connect("database.db")
        res = conn.execute(
            """
            SELECT
                username, time, update_time, create_time
            FROM
                rank
            WHERE
                checkpoint = ?
            ORDER BY
                time
            """,
            (str(checkpoint),)
        ).fetchall()
        conn.close()
        ret = [{"username": r[0], "time": r[1], "update_time": r[2], "create_time": r[3]} for r in res]
        return {"code": 1, "message": "success", "data": ret}

    def post(self, checkpoint):
        args = parser.parse_args()
        username = args["username"]
        time = args["time"]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        res = cur.execute(
            """
            SELECT
                time
            FROM
                rank
            WHERE
                username = ? AND checkpoint = ?
            """,
            (username,checkpoint)
        ).fetchone()
        if res == None:
            cur.execute(
                """
                INSERT INTO
                    rank (username, checkpoint, time, update_time, create_time)
                VALUES
                    (?,?,?,datetime('now'),datetime('now'))
                """,
                (username,checkpoint,time)
            )
        elif res[0] > time:
            cur.execute(
                """
                UPDATE
                    rank
                SET
                    time = ?,
                    update_time = datetime('now')
                WHERE
                    username = ? AND checkpoint = ?
                """,
                (time,username,checkpoint)
            )
        con.commit()
        con.close()
        return {"code": 1, "message": "success", "data": None}

if __name__ == "__main__":
    api.add_resource(Rank, "/rank/<checkpoint>")
    app.run()

