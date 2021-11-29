from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
import resolvers as r

app = Flask(__name__)

type_defs = load_schema_from_path('schema.graphql')

query = QueryType()
building = ObjectType('Building')
resident = ObjectType('Resident')

query.set_field('building_with_id', r.building_with_id)
building.set_field('residents', r.resolve_residents_in_building)

schema = make_executable_schema(type_defs, [building, resident, query])

@app.route('/graphql', methods = ['GET'])
def playground():
    return PLAYGROUND_HTML, 200

@app.route('/graphql', methods = ['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value = None,
        debug = app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

