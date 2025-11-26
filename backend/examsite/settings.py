#         "CONN_MAX_AGE": 60,
#     }
#     "default": dj_database_url.config(
#         default=os.getenv("DATABASE_URL"),
#         conn_max_age=600,
#         ssl_require=True
#     )
# }

# Prefer DATABASE_URL; if missing, build from individual envs
db_url = os.getenv("DATABASE_URL")
if not db_url:
    db_url = (
        f"postgresql://{os.getenv('POSTGRES_USER','examuser')}:"
        f"{os.getenv('POSTGRES_PASSWORD','examsecret')}@"
        f"{os.getenv('DB_HOST','exam_db')}:"
        f"{os.getenv('DB_PORT','5432')}/"
        f"{os.getenv('POSTGRES_DB','examdb')}"
    )

DATABASES = {
    "default": dj_database_url.parse(
        db_url,
        conn_max_age=600,
        ssl_require=False  # local docker postgres doesn't use SSL
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ.get("TIME_ZONE", "Asia/Ho_Chi_Minh")
USE_TZ = True

USE_I18N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")