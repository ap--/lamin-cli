import lamindb as ln

ln.settings.sync_git_repo = "https://github.com/laminlabs/lamin-cli"
ln.transform.stem_uid = "m5uCHTTpJnjQ"
ln.transform.version = "1"

ln.connect("lamindb-unit-tests")

if __name__ == "__main__":
    # we're using new_run here to mock the notebook situation
    # and cover the look up of an existing run in the tests
    # new_run = True is trivial
    ln.track(new_run=False)

    print("hello!")
