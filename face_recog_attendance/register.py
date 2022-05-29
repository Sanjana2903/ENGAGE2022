from base64 import b64decode
import os
import pickle
import face_recognition as fr


def register_on_submit(email, image):
    header, encoded = image.split(",", 1)

    with open("registering.png", "wb") as f:
        f.write(b64decode(encoded))

    try:
        try:
            data = pickle.loads(open("data.pickle", "rb").read())
        except Exception as e:
            # print(e.__cause__)
            data = dict()
            with open("data.pickle", "wb") as f:
                f.write(pickle.dumps(data))

        data = pickle.loads(open("data.pickle", "rb").read())

        if email in data.keys():
            return "This user ID is already registered"

        got_image = fr.load_image_file("registering.png")
        face_locations = fr.face_locations(got_image)
        if len(face_locations) == 0:
            return "No face detected"
        if len(face_locations) > 1:
            return "Multiple faces detected"

        data[email] = encoded
        with open("data.pickle", "wb") as f:
            f.write(pickle.dumps(data))
    except Exception as e:
        # print(e.__cause__)
        return "Registration failed !"
    return "Registration Successful"
