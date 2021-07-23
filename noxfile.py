import nox


PYTHON_FILES = [
    "noxfile.py",
]

@nox.session(reuse_venv=True)
def gendoc(session):
    session.install("sphinx", "sphinx-rtd-theme")
    session.install("-e", ".")
    session.run("sphinx-build", "-M", "html", ".", "build")
