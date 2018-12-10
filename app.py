from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application
app = Flask(__name__)
app.config['DEBUG'] = True


# Initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


# Create data storage
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    attribut = db.Column(db.String(20), nullable=False)
    type = "Skill"
    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        return {
            'attribut': self.attribut,
            'id': self.id,
            'type': self.type,
        }

db.create_all()

@app.route('/',methods=['GET'])
def test():
    return jsonify({'message':'It works!'})
#list the skills
@app.route('/skills',methods=['GET'])
def returnALL():
    res = db.session.query(Skill).all()
    temp = []
    for x in res:
        temp.append(x.to_json())
    return jsonify(object = temp)

#list a skill
@app.route('/skills/<int:id>',methods=['GET'])
def returnOne(id):
    res = db.session.query(Skill).filter_by(id = id)
    temp = []
    for x in res:
        temp.append(x.to_json())
    return jsonify(object = temp)

#add a skill
@app.route('/skills',methods=['POST'])
def addOne():
    if not request.json or not "attribut" in request.json:
        abort(400)
    skill = Skill(attribut = request.json["attribut"])
    db.session.add(skill)
    db.session.commit()
    res = db.session.query(Skill).all()
    temp = []
    for x in res:
        temp.append(x.to_json())
    return jsonify(object = temp), 201

#modifier a skill
@app.route('/skills/<int:id>',methods=['PUT'])
def editOne(id):
    if not request.json:
        abort(400)
    res = db.session.query(Skill).filter(Skill.id == id)
    res.update({Skill.attribut : request.json["attribut"]})
    db.session.commit()
    temp = []
    for x in res:
        temp.append(x.to_json())
    return jsonify(object = temp)

#delete a skill
@app.route('/skills/<int:id>',methods=['DELETE'])
def removeOne(id):
    if not request.json:
        abort(400)
    res = db.session.query(Skill).get(id)
    db.session.delete(res)
    db.session.commit()
    res = db.session.query(Skill).all()
    temp = []
    for x in res:
        temp.append(x.to_json())
    return jsonify(object=temp)

if __name__ == '__main__':
    app.run(debug=True)
