from apps.corporations.models import Corporation
from apps.person.models import Person, Affiliation

def unique_lines(infile):
    """ Returns the unique lines in infile. Used for filtering out
    duplicate names in a list of company owners."""
    unique = set()
    for line in infile:
        unique.add(line)
    return unique

def do_lookup(infile,outfile):
    """ Quick script for finding all the companies associated with a given
    person's name. Since there are often multiple people with the same name,
    the output is grouped by personal id numbers, which are unique."""
    names = unique_lines(infile)

    for n in names:
        pers = Person.objects.filter(name=n.strip())
        for p in pers:
            result = set()
            for corp in p.affiliations.all():
                dl=u"|"
                output = (p.name or u"")+dl+\
                         (p.personal_code or u"")+dl+\
                         (corp.name or u"")+dl+\
                         (corp.id_code or u"")+u"\n"
                result.add(output)
            for l in result:
                outfile.write(l)
