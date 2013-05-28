from fabric.api import local, cd, run, env
from fabric.operations import put

def dumpdb(user,db):
    """ Dumps the local db to a plaintext file suitable for import."""
    local("pg_dump --clean -h localhost -U {} {} > dump.sql".format(user,db))

def compressdb(dbfile="dump.sql"):
    """ Compresses the dumped db using tar."""
    local("tar czf {}.tar.gz {}".format(dbfile,dbfile))

def uploaddb(dbfile="dump.sql.tar.gz"):
    """ Uploads the compressed db file, uncompresses it remotely, and deletes
    the remote compressed file."""
    put(dbfile,dbfile)
    run("tar xzf {}".format(dbfile))
    run("rm {}".format(dbfile))

def importdb(user,db,dbfile="dump.sql"):
    """ Remotely imports the db file, then deletes it."""
    run("ionice -c2 -n6 psql -U {} {} < {}".format(user,db,dbfile))
    run("rm {}".format(dbfile))

def cleanup(dbfile="dump.sql"):
    """ Local cleanup. """
    local("rm {}".format(dbfile))
    local("rm {}.tar.gz".format(dbfile))
