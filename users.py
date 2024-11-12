from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

import main


users_router = APIRouter(tags=["User"])


@users_router.get("/users/get-all")
def get_all_users():
    main.cursor.execute("""SELECT * FROM USERS""")
    users = main.cursor.fetchall()

    return users


@users_router.get("/users/by-id/{id}")
def get_user_by_id(id: int):
    main.cursor.execute("""SELECT * FROM USERS WHERE user_id=%s""",
                        (id,))

    user = main.cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id '{id}' was not found!"
        )

    return user


@users_router.get("/users/by-email/{email}")
def get_user_by_id(email: str):
    main.cursor.execute("""SELECT * FROM USERS WHERE email=%s""",
                        (email,))

    user = main.cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email '{email}' was not found!"
        )

    return user