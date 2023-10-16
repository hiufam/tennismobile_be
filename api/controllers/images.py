from uuid import uuid1

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from ..models.image import Image
from ..database import session

images = Blueprint('images', __name__, url_prefix='/api/images')

@images.post('/')
@jwt_required()
def upload_image():
    image_file = request.files['image']
    
    image_name = image_file.filename.split('.')[0]
    image_extension = image_file.filename.split('.')[1]
    image_name = uuid1()

    image_path = f'./images/{str(image_name)}.{image_extension}'
    
    image_file.save(image_path)

    new_image = Image(
        url=image_path
    )

    session.add(new_image)
    session.commit()

    return jsonify({
        'image': {
            'image_id': new_image.id,
            'image_url': new_image.url,
        }
    }), 200