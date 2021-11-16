from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import time
import numpy as np
import pandas as pd
import argparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
# app.config['SECRET_KEY'] = 'cairocoders-ednalan'

db = SQLAlchemy(app)

# app.jinja_env.variable_start_string = '%%'
# app.jinja_env.variable_end_string = '%%'


# class Employees(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fullname = db.Column(db.String(150))
#     position = db.Column(db.String(150))
#     office = db.Column(db.String(150))
#     age = db.Column(db.Integer)
#     startdate = db.Column(db.String(150))
#     salary = db.Column(db.String(150))


class Arabidopsis_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))


class Banana_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))


class Betavulgaris_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Bostaurus_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Brachypodiumdistachyon_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Brassicarapa_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Fly_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Glycinemax_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Medaka_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))


class Solanumlycopersicum_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))


class Sorghumbicolor_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))


class Triticumaestivum_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Susscrofa_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Vitisviniferas_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Worm_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))


class Zeamays_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Zebrafish_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))


class Rat_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Rabbit_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Opossum_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))


class Mouse_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Macaque_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Human_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Chicken_gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chromosome = db.Column(db.Integer)
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Biotype = db.Column(db.String(200))
    Tissue = db.Column(db.String(200))
    Species = db.Column(db.String(200))
    Project = db.Column(db.String(200))

class Gene_expression(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Stage = db.Column(db.String(200))
    Expression = db.Column(db.Integer)

class Gene_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Chr = db.Column(db.String(200))
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Gene_name = db.Column(db.String(200))
    Gene_type = db.Column(db.String(200))
    Description = db.Column(db.String(2000))


class Go_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    Go_function = db.Column(db.String(2000))
    Go_id = db.Column(db.String(200))

class TF_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Gene = db.Column(db.String(200))
    TF = db.Column(db.String(200))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/summary/')
def summary():
    return render_template("summary.html")

@app.route('/download/')
def download():
    return render_template("download.html")

@app.route('/help/')
def help():
    return render_template("help.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

# @app.route('/rat/<Gene>', methods=['GET'])
# def rat(Gene):
#     exp = Gene_expression.query.filter(
#         or_(Gene_expression.Gene == Gene))
#     return render_template("rat_gene.html", exp=exp)

@app.route('/chi/')
def chi():
    return render_template("table_chicken.html")

@app.route('/hum/')
def hum():
    return render_template("table_human.html")

@app.route('/mac/')
def mac():
    return render_template("table_macaque.html")

@app.route('/mou/')
def mou():
    return render_template("table_mouse.html")


@app.route('/opo/')
def opo():
    return render_template("table_opossum.html")

@app.route('/rab/')
def rab():
    return render_template("table_rabbit.html")

@app.route('/rat/')
def rat():
    return render_template("table_rat.html")




@app.route('/ara/')
def ara():
    return render_template("table_ara.html")

@app.route('/ban/')
def ban():
    return render_template("table_ban.html")

@app.route('/beta/')
def beta():
    return render_template("table_beta.html")

@app.route('/bos/')
def bos():
    return render_template("table_bos.html")



@app.route('/brac/')
def brac():
    return render_template("table_brac.html")

@app.route('/bras/')
def bras():
    return render_template("table_bras.html")

@app.route('/fly/')
def fly():
    return render_template("table_fly.html")

@app.route('/gly/')
def gly():
    return render_template("table_gly.html")



@app.route('/med/')
def med():
    return render_template("table_med.html")

@app.route('/sol/')
def sol():
    return render_template("table_sol.html")

@app.route('/sor/')
def sor():
    return render_template("table_sor.html")

@app.route('/sus/')
def sus():
    return render_template("table_sus.html")




@app.route('/tri/')
def tri():
    return render_template("table_tri.html")

@app.route('/vit/')
def vit():
    return render_template("table_vit.html")

@app.route('/worm/')
def worm():
    return render_template("table_worm.html")

@app.route('/zea/')
def zea():
    return render_template("table_zea.html")

@app.route('/zeb/')
def zeb():
    return render_template("table_zebrafish.html")


@app.route('/rat_json/', methods=['GET', 'POST'])
def rat_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Rat_gene.query.order_by(getattr(Rat_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Rat_gene.query.order_by(getattr(Rat_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Rat_gene.query.filter(
                or_(Rat_gene.Gene.like(search), Rat_gene.Chromosome.like(search),
                    Rat_gene.Biotype.like(search), Rat_gene.Tissue.like(search),
                    Rat_gene.Species.like(search),
                    Rat_gene.Project.like(search))).order_by(
                getattr(Rat_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Rat_gene.query.filter(
                or_(Rat_gene.Gene.like(search), Rat_gene.Chromosome.like(search),
                    Rat_gene.Biotype.like(search), Rat_gene.Tissue.like(search),
                    Rat_gene.Species.like(search),
                    Rat_gene.Project.like(search))).order_by(
                getattr(Rat_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/rabbit_json/', methods=['GET', 'POST'])
def rabbit_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Rabbit_gene.query.order_by(getattr(Rabbit_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Rabbit_gene.query.order_by(getattr(Rabbit_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Rabbit_gene.query.filter(
                or_(Rabbit_gene.Gene.like(search), Rabbit_gene.Chromosome.like(search),
                    Rabbit_gene.Biotype.like(search), Rabbit_gene.Tissue.like(search),
                    Rabbit_gene.Species.like(search),
                    Rabbit_gene.Project.like(search))).order_by(
                getattr(Rabbit_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Rabbit_gene.query.filter(
                or_(Rabbit_gene.Gene.like(search), Rabbit_gene.Chromosome.like(search),
                    Rabbit_gene.Biotype.like(search), Rabbit_gene.Tissue.like(search),
                    Rabbit_gene.Species.like(search),
                    Rabbit_gene.Project.like(search))).order_by(
                getattr(Rabbit_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst

@app.route('/opossum_json/', methods=['GET', 'POST'])
def opossum_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Opossum_gene.query.order_by(getattr(Opossum_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Opossum_gene.query.order_by(getattr(Opossum_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Opossum_gene.query.filter(
                or_(Opossum_gene.Gene.like(search), Opossum_gene.Chromosome.like(search),
                    Opossum_gene.Biotype.like(search), Opossum_gene.Tissue.like(search),
                    Opossum_gene.Species.like(search),
                    Opossum_gene.Project.like(search))).order_by(
                getattr(Opossum_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Opossum_gene.query.filter(
                or_(Opossum_gene.Gene.like(search), Opossum_gene.Chromosome.like(search),
                    Opossum_gene.Biotype.like(search), Opossum_gene.Tissue.like(search),
                    Opossum_gene.Species.like(search),
                    Opossum_gene.Project.like(search))).order_by(
                getattr(Opossum_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst

@app.route('/macaque_json/', methods=['GET', 'POST'])
def macaque_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Macaque_gene.query.order_by(getattr(Macaque_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Macaque_gene.query.order_by(getattr(Macaque_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Macaque_gene.query.filter(
                or_(Macaque_gene.Gene.like(search), Macaque_gene.Chromosome.like(search),
                    Macaque_gene.Biotype.like(search), Macaque_gene.Tissue.like(search),
                    Macaque_gene.Species.like(search),
                    Macaque_gene.Project.like(search))).order_by(
                getattr(Macaque_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Macaque_gene.query.filter(
                or_(Macaque_gene.Gene.like(search), Macaque_gene.Chromosome.like(search),
                    Macaque_gene.Biotype.like(search), Macaque_gene.Tissue.like(search),
                    Macaque_gene.Species.like(search),
                    Macaque_gene.Project.like(search))).order_by(
                getattr(Macaque_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst



@app.route('/human_json/', methods=['GET', 'POST'])
def human_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Human_gene.query.order_by(getattr(Human_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Human_gene.query.order_by(getattr(Human_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Human_gene.query.filter(
                or_(Human_gene.Gene.like(search), Human_gene.Chromosome.like(search),
                    Human_gene.Biotype.like(search), Human_gene.Tissue.like(search),
                    Human_gene.Species.like(search),
                    Human_gene.Project.like(search))).order_by(
                getattr(Human_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Human_gene.query.filter(
                or_(Human_gene.Gene.like(search), Human_gene.Chromosome.like(search),
                    Human_gene.Biotype.like(search), Human_gene.Tissue.like(search),
                    Human_gene.Species.like(search),
                    Human_gene.Project.like(search))).order_by(
                getattr(Human_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/chicken_json/', methods=['GET', 'POST'])
def chicken_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Chicken_gene.query.order_by(getattr(Chicken_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Chicken_gene.query.order_by(getattr(Chicken_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Chicken_gene.query.filter(
                or_(Chicken_gene.Gene.like(search), Chicken_gene.Chromosome.like(search),
                    Chicken_gene.Biotype.like(search), Chicken_gene.Tissue.like(search),
                    Chicken_gene.Species.like(search),
                    Chicken_gene.Project.like(search))).order_by(
                getattr(Chicken_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Chicken_gene.query.filter(
                or_(Chicken_gene.Gene.like(search), Chicken_gene.Chromosome.like(search),
                    Chicken_gene.Biotype.like(search), Chicken_gene.Tissue.like(search),
                    Chicken_gene.Species.like(search),
                    Chicken_gene.Project.like(search))).order_by(
                getattr(Mouse_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/mouse_json/', methods=['GET', 'POST'])
def mouse_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Mouse_gene.query.order_by(getattr(Mouse_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Mouse_gene.query.order_by(getattr(Mouse_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Mouse_gene.query.filter(
                or_(Mouse_gene.Gene.like(search), Mouse_gene.Chromosome.like(search),
                    Mouse_gene.Biotype.like(search), Mouse_gene.Tissue.like(search),
                    Mouse_gene.Species.like(search),
                    Mouse_gene.Project.like(search))).order_by(
                getattr(Mouse_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Mouse_gene.query.filter(
                or_(Mouse_gene.Gene.like(search), Mouse_gene.Chromosome.like(search),
                    Mouse_gene.Biotype.like(search), Mouse_gene.Tissue.like(search),
                    Mouse_gene.Species.like(search),
                    Mouse_gene.Project.like(search))).order_by(
                getattr(Mouse_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


######################################################################
@app.route('/ara_json/', methods=['GET', 'POST'])
def ara_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Arabidopsis_gene.query.order_by(getattr(Arabidopsis_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Arabidopsis_gene.query.order_by(getattr(Arabidopsis_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Arabidopsis_gene.query.filter(
                or_(Arabidopsis_gene.Gene.like(search), Arabidopsis_gene.Chromosome.like(search),
                    Arabidopsis_gene.Biotype.like(search), Arabidopsis_gene.Tissue.like(search),
                    Arabidopsis_gene.Species.like(search),
                    Arabidopsis_gene.Project.like(search))).order_by(
                getattr(Arabidopsis_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Arabidopsis_gene.query.filter(
                or_(Arabidopsis_gene.Gene.like(search), Arabidopsis_gene.Chromosome.like(search),
                    Arabidopsis_gene.Biotype.like(search), Arabidopsis_gene.Tissue.like(search),
                    Arabidopsis_gene.Species.like(search),
                    Arabidopsis_gene.Project.like(search))).order_by(
                getattr(Arabidopsis_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/ban_json/', methods=['GET', 'POST'])
def ban_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Banana_gene.query.order_by(getattr(Banana_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Banana_gene.query.order_by(getattr(Banana_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Banana_gene.query.filter(
                or_(Banana_gene.Gene.like(search), Banana_gene.Chromosome.like(search),
                    Banana_gene.Biotype.like(search), Banana_gene.Tissue.like(search),
                    Banana_gene.Species.like(search),
                    Banana_gene.Project.like(search))).order_by(
                getattr(Banana_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Banana_gene.query.filter(
                or_(Banana_gene.Gene.like(search), Banana_gene.Chromosome.like(search),
                    Banana_gene.Biotype.like(search), Banana_gene.Tissue.like(search),
                    Banana_gene.Species.like(search),
                    Banana_gene.Project.like(search))).order_by(
                getattr(Banana_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/beta_json/', methods=['GET', 'POST'])
def beta_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Betavulgaris_gene.query.order_by(getattr(Betavulgaris_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Betavulgaris_gene.query.order_by(getattr(Betavulgaris_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Betavulgaris_gene.query.filter(
                or_(Betavulgaris_gene.Gene.like(search), Betavulgaris_gene.Chromosome.like(search),
                    Betavulgaris_gene.Biotype.like(search), Betavulgaris_gene.Tissue.like(search),
                    Betavulgaris_gene.Species.like(search),
                    Betavulgaris_gene.Project.like(search))).order_by(
                getattr(Betavulgaris_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Betavulgaris_gene.query.filter(
                or_(Betavulgaris_gene.Gene.like(search), Betavulgaris_gene.Chromosome.like(search),
                    Betavulgaris_gene.Biotype.like(search), Betavulgaris_gene.Tissue.like(search),
                    Betavulgaris_gene.Species.like(search),
                    Betavulgaris_gene.Project.like(search))).order_by(
                getattr(Betavulgaris_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/bos_json/', methods=['GET', 'POST'])
def bos_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Bostaurus_gene.query.order_by(getattr(Bostaurus_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Bostaurus_gene.query.order_by(getattr(Bostaurus_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Bostaurus_gene.query.filter(
                or_(Bostaurus_gene.Gene.like(search), Bostaurus_gene.Chromosome.like(search),
                    Bostaurus_gene.Biotype.like(search), Bostaurus_gene.Tissue.like(search),
                    Bostaurus_gene.Species.like(search),
                    Bostaurus_gene.Project.like(search))).order_by(
                getattr(Bostaurus_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Bostaurus_gene.query.filter(
                or_(Bostaurus_gene.Gene.like(search), Bostaurus_gene.Chromosome.like(search),
                    Bostaurus_gene.Biotype.like(search), Bostaurus_gene.Tissue.like(search),
                    Bostaurus_gene.Species.like(search),
                    Bostaurus_gene.Project.like(search))).order_by(
                getattr(Bostaurus_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst

@app.route('/brac_json/', methods=['GET', 'POST'])
def brac_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Brachypodiumdistachyon_gene.query.order_by(getattr(Brachypodiumdistachyon_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Brachypodiumdistachyon_gene.query.order_by(getattr(Brachypodiumdistachyon_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Brachypodiumdistachyon_gene.query.filter(
                or_(Brachypodiumdistachyon_gene.Gene.like(search), Brachypodiumdistachyon_gene.Chromosome.like(search),
                    Brachypodiumdistachyon_gene.Biotype.like(search), Brachypodiumdistachyon_gene.Tissue.like(search),
                    Brachypodiumdistachyon_gene.Species.like(search),
                    Brachypodiumdistachyon_gene.Project.like(search))).order_by(
                getattr(Brachypodiumdistachyon_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Brachypodiumdistachyon_gene.query.filter(
                or_(Brachypodiumdistachyon_gene.Gene.like(search), Brachypodiumdistachyon_gene.Chromosome.like(search),
                    Brachypodiumdistachyon_gene.Biotype.like(search), Brachypodiumdistachyon_gene.Tissue.like(search),
                    Brachypodiumdistachyon_gene.Species.like(search),
                    Brachypodiumdistachyon_gene.Project.like(search))).order_by(
                getattr(Brachypodiumdistachyon_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/bras_json/', methods=['GET', 'POST'])
def bras_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Brassicarapa_gene.query.order_by(getattr(Brassicarapa_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Brassicarapa_gene.query.order_by(getattr(Brassicarapa_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Brassicarapa_gene.query.filter(
                or_(Brassicarapa_gene.Gene.like(search), Brassicarapa_gene.Chromosome.like(search),
                    Brassicarapa_gene.Biotype.like(search), Brassicarapa_gene.Tissue.like(search),
                    Brassicarapa_gene.Species.like(search),
                    Brassicarapa_gene.Project.like(search))).order_by(
                getattr(Brassicarapa_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Brassicarapa_gene.query.filter(
                or_(Brassicarapa_gene.Gene.like(search), Brassicarapa_gene.Chromosome.like(search),
                    Brassicarapa_gene.Biotype.like(search), Brassicarapa_gene.Tissue.like(search),
                    Brassicarapa_gene.Species.like(search),
                    Brassicarapa_gene.Project.like(search))).order_by(
                getattr(Brassicarapa_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/fly_json/', methods=['GET', 'POST'])
def fly_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Fly_gene.query.order_by(getattr(Fly_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Fly_gene.query.order_by(getattr(Fly_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Fly_gene.query.filter(
                or_(Fly_gene.Gene.like(search), Fly_gene.Chromosome.like(search),
                    Fly_gene.Biotype.like(search), Fly_gene.Tissue.like(search),
                    Fly_gene.Species.like(search),
                    Fly_gene.Project.like(search))).order_by(
                getattr(Fly_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Fly_gene.query.filter(
                or_(Fly_gene.Gene.like(search), Fly_gene.Chromosome.like(search),
                    Fly_gene.Biotype.like(search), Fly_gene.Tissue.like(search),
                    Fly_gene.Species.like(search),
                    Fly_gene.Project.like(search))).order_by(
                getattr(Fly_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst

#############################################################################
@app.route('/gly_json/', methods=['GET', 'POST'])
def gly_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Glycinemax_gene.query.order_by(getattr(Glycinemax_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Glycinemax_gene.query.order_by(getattr(Glycinemax_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Glycinemax_gene.query.filter(
                or_(Glycinemax_gene.Gene.like(search), Glycinemax_gene.Chromosome.like(search),
                    Glycinemax_gene.Biotype.like(search), Glycinemax_gene.Tissue.like(search),
                    Glycinemax_gene.Species.like(search),
                    Glycinemax_gene.Project.like(search))).order_by(
                getattr(Glycinemax_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Glycinemax_gene.query.filter(
                or_(Glycinemax_gene.Gene.like(search), Glycinemax_gene.Chromosome.like(search),
                    Glycinemax_gene.Biotype.like(search), Glycinemax_gene.Tissue.like(search),
                    Glycinemax_gene.Species.like(search),
                    Glycinemax_gene.Project.like(search))).order_by(
                getattr(Glycinemax_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst

@app.route('/med_json/', methods=['GET', 'POST'])
def med_json():
    Medaka_gene
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Medaka_gene.query.order_by(getattr(Medaka_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Medaka_gene.query.order_by(getattr(Medaka_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Medaka_gene.query.filter(
                or_(Medaka_gene.Gene.like(search), Medaka_gene.Chromosome.like(search),
                    Medaka_gene.Biotype.like(search), Medaka_gene.Tissue.like(search),
                    Medaka_gene.Species.like(search),
                    Medaka_gene.Project.like(search))).order_by(
                getattr(Medaka_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Medaka_gene.query.filter(
                or_(Medaka_gene.Gene.like(search), Medaka_gene.Chromosome.like(search),
                    Medaka_gene.Biotype.like(search), Medaka_gene.Tissue.like(search),
                    Medaka_gene.Species.like(search),
                    Medaka_gene.Project.like(search))).order_by(
                getattr(Medaka_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/sol_json/', methods=['GET', 'POST'])
def sol_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Solanumlycopersicum_gene.query.order_by(getattr(Solanumlycopersicum_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Solanumlycopersicum_gene.query.order_by(getattr(Solanumlycopersicum_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Solanumlycopersicum_gene.query.filter(
                or_(Solanumlycopersicum_gene.Gene.like(search), Solanumlycopersicum_gene.Chromosome.like(search),
                    Solanumlycopersicum_gene.Biotype.like(search), Solanumlycopersicum_gene.Tissue.like(search),
                    Solanumlycopersicum_gene.Species.like(search), Solanumlycopersicum_gene.Project.like(search))).order_by(
                getattr(Solanumlycopersicum_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Solanumlycopersicum_gene.query.filter(
                or_(Solanumlycopersicum_gene.Gene.like(search), Solanumlycopersicum_gene.Chromosome.like(search),
                    Solanumlycopersicum_gene.Biotype.like(search), Solanumlycopersicum_gene.Tissue.like(search),
                    Solanumlycopersicum_gene.Species.like(search), Solanumlycopersicum_gene.Project.like(search))).order_by(
                getattr(Solanumlycopersicum_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/sor_json/', methods=['GET', 'POST'])
def sor_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Sorghumbicolor_gene.query.order_by(getattr(Sorghumbicolor_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Sorghumbicolor_gene.query.order_by(getattr(Sorghumbicolor_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Sorghumbicolor_gene.query.filter(
                or_(Sorghumbicolor_gene.Gene.like(search), Sorghumbicolor_gene.Chromosome.like(search),
                    Sorghumbicolor_gene.Biotype.like(search), Sorghumbicolor_gene.Tissue.like(search),
                    Sorghumbicolor_gene.Species.like(search), Sorghumbicolor_gene.Project.like(search))).order_by(
                getattr(Sorghumbicolor_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Sorghumbicolor_gene.query.filter(
                or_(Sorghumbicolor_gene.Gene.like(search), Sorghumbicolor_gene.Chromosome.like(search),
                    Sorghumbicolor_gene.Biotype.like(search), Sorghumbicolor_gene.Tissue.like(search),
                    Sorghumbicolor_gene.Species.like(search), Sorghumbicolor_gene.Project.like(search))).order_by(
                getattr(Sorghumbicolor_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst

@app.route('/sus_json/', methods=['GET', 'POST'])
def sus_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Susscrofa_gene.query.order_by(getattr(Susscrofa_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Susscrofa_gene.query.order_by(getattr(Susscrofa_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Susscrofa_gene.query.filter(
                or_(Susscrofa_gene.Gene.like(search), Susscrofa_gene.Chromosome.like(search),
                    Susscrofa_gene.Biotype.like(search), Susscrofa_gene.Tissue.like(search),
                    Susscrofa_gene.Species.like(search), Susscrofa_gene.Project.like(search))).order_by(
                getattr(Susscrofa_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Susscrofa_gene.query.filter(
                or_(Susscrofa_gene.Gene.like(search), Susscrofa_gene.Chromosome.like(search),
                    Susscrofa_gene.Biotype.like(search), Susscrofa_gene.Tissue.like(search),
                    Susscrofa_gene.Species.like(search), Susscrofa_gene.Project.like(search))).order_by(
                getattr(Susscrofa_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/tri_json/', methods=['GET', 'POST'])
def tri_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Triticumaestivum_gene.query.order_by(getattr(Triticumaestivum_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Triticumaestivum_gene.query.order_by(getattr(Triticumaestivum_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Triticumaestivum_gene.query.filter(
                or_(Triticumaestivum_gene.Gene.like(search), Triticumaestivum_gene.Chromosome.like(search),
                    Triticumaestivum_gene.Biotype.like(search), Triticumaestivum_gene.Tissue.like(search),
                    Triticumaestivum_gene.Species.like(search), Triticumaestivum_gene.Project.like(search))).order_by(
                getattr(Triticumaestivum_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Triticumaestivum_gene.query.filter(
                or_(Triticumaestivum_gene.Gene.like(search), Triticumaestivum_gene.Chromosome.like(search),
                    Triticumaestivum_gene.Biotype.like(search), Triticumaestivum_gene.Tissue.like(search),
                    Triticumaestivum_gene.Species.like(search), Triticumaestivum_gene.Project.like(search))).order_by(
                getattr(Triticumaestivum_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst



@app.route('/vit_json/', methods=['GET', 'POST'])
def vit_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Vitisviniferas_gene.query.order_by(getattr(Vitisviniferas_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Vitisviniferas_gene.query.order_by(getattr(Vitisviniferas_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Vitisviniferas_gene.query.filter(
                or_(Vitisviniferas_gene.Gene.like(search), Vitisviniferas_gene.Chromosome.like(search),
                    Vitisviniferas_gene.Biotype.like(search), Vitisviniferas_gene.Tissue.like(search),
                    Vitisviniferas_gene.Species.like(search), Vitisviniferas_gene.Project.like(search))).order_by(
                getattr(Vitisviniferas_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Vitisviniferas_gene.query.filter(
                or_(Vitisviniferas_gene.Gene.like(search), Vitisviniferas_gene.Chromosome.like(search),
                    Vitisviniferas_gene.Biotype.like(search), Vitisviniferas_gene.Tissue.like(search),
                    Vitisviniferas_gene.Species.like(search), Vitisviniferas_gene.Project.like(search))).order_by(
                getattr(Vitisviniferas_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/worm_json/', methods=['GET', 'POST'])
def worm_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Worm_gene.query.order_by(getattr(Worm_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Worm_gene.query.order_by(getattr(Worm_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Worm_gene.query.filter(
                or_(Worm_gene.Gene.like(search), Worm_gene.Chromosome.like(search),
                    Worm_gene.Biotype.like(search), Worm_gene.Tissue.like(search),
                    Worm_gene.Species.like(search), Worm_gene.Project.like(search))).order_by(
                getattr(Worm_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Worm_gene.query.filter(
                or_(Worm_gene.Gene.like(search), Worm_gene.Chromosome.like(search),
                    Worm_gene.Biotype.like(search), Worm_gene.Tissue.like(search),
                    Worm_gene.Species.like(search), Worm_gene.Project.like(search))).order_by(
                getattr(Worm_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst


@app.route('/zea_json/', methods=['GET', 'POST'])
def zea_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Zeamays_gene.query.order_by(getattr(Zeamays_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Zeamays_gene.query.order_by(getattr(Zeamays_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Zeamays_gene.query.filter(
                or_(Zeamays_gene.Gene.like(search), Zeamays_gene.Chromosome.like(search),
                    Zeamays_gene.Biotype.like(search), Zeamays_gene.Tissue.like(search),
                    Zeamays_gene.Species.like(search), Zeamays_gene.Project.like(search))).order_by(
                getattr(Zeamays_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Zeamays_gene.query.filter(
                or_(Zeamays_gene.Gene.like(search), Zeamays_gene.Chromosome.like(search),
                    Zeamays_gene.Biotype.like(search), Zeamays_gene.Tissue.like(search),
                    Zeamays_gene.Species.like(search), Zeamays_gene.Project.like(search))).order_by(
                getattr(Zeamays_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst

@app.route('/zeb_json/', methods=['GET', 'POST'])
def zeb_json():
    pp = request.args.to_dict()
    page = pp['start']
    pageSize = 15
    page_skip = int(page) * pageSize
    tag = pp['search[value]']
    search = "%{}%".format(tag)
    sortnum = pp['order[0][column]']
    dir = pp['order[0][dir]']
    ele = pp['columns[' + str(sortnum) + '][data]']
    if search == "":
        if dir == 'desc':
            rrr = Zebrafish_gene.query.order_by(getattr(Zebrafish_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Zebrafish_gene.query.order_by(getattr(Zebrafish_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
    else:
        if dir == 'desc':
            rrr = Zebrafish_gene.query.filter(
                or_(Zebrafish_gene.Gene.like(search), Zebrafish_gene.Chromosome.like(search),
                    Zebrafish_gene.Biotype.like(search), Zebrafish_gene.Tissue.like(search),
                    Zebrafish_gene.Species.like(search), Zebrafish_gene.Project.like(search))).order_by(
                getattr(Zebrafish_gene, ele).desc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()
        else:
            rrr = Zebrafish_gene.query.filter(
                or_(Zebrafish_gene.Gene.like(search), Zebrafish_gene.Chromosome.like(search),
                    Zebrafish_gene.Biotype.like(search), Zebrafish_gene.Tissue.like(search),
                    Zebrafish_gene.Species.like(search), Zebrafish_gene.Project.like(search))).order_by(
                getattr(Zebrafish_gene, ele).asc())
            count_num = rrr.count()
            result = rrr.offset(page_skip).limit(pageSize).all()

    alldata = []
    for one in result:
        data = {"id": one.id, "Gene": one.Gene, "Chromosome": one.Chromosome, "Start": one.Start,
                "End": one.End, "Biotype": one.Biotype, "Tissue": one.Tissue, "Species": one.Species,
                "Project": one.Project}
        alldata.append(data)
    rst = {}
    rst["draw"] = pp["draw"]
    rst["recordsTotal"] = count_num
    rst["recordsFiltered"] = count_num
    rst["data"] = alldata
    print(rst)

    return rst

@app.route('/single_gene/<Gene>')
def single_gene(Gene):
    info = Gene_info.query.filter(
        or_(Gene_info.Gene == Gene))
    Goinfo = Go_info.query.filter(
        or_(Go_info.Gene == Gene))
    TF = TF_info.query.filter(
        or_(TF_info.Gene == Gene))
    # exp = Gene_expression.query.filter(
    #     or_(Gene_expression.Gene == Gene))
    return render_template("single_gene.html",info=info,Goinfo=Goinfo,TF=TF)

@app.route('/test/')
def test():
    aa = 'tes'
    return render_template("test.html",aa=aa)

if __name__ == '__main__':
    app.run(debug=True,port=8006)
