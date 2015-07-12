#!/usr/bin/env python3

import argparse
import collections
import configparser
import re
import sys

SKILL_OPTIONS = ['level1', 'level2', 'level3', 'level4', 'level5', 'Omega']
KNOWLEDGE_SKILL_OPTIONS = ['level1', 'level2', 'level3', 'level4', 'level5',
                           'Further', 'Greater', 'Omega']


def tex_to_ini(tex):
    """
    function that grabs the configuration for skills from the tex file

    params:
        str tex - contents of a tex file containing skills
    returns:
        ConfigParser ini - ini version of the tex
    """
    # RegEx that do the magic
    section_experssion = \
        re.compile(r'\\section\{(?P<name>.+?)\}(?P<disc>.+?)' +
                   r'(?=((?:\\k?skill)|(?:\\section)))', re.DOTALL)

    skills_expression = \
        re.compile(r'\\skill(?P<name>\{.*?\})(?P<level1>\{.*?\})' +
                   r'(?P<level2>\{.*?\})(?P<level3>\{.*?\})' +
                   r'(?P<level4>\{.*?\})(?P<level5>\{.*?\})(?P<Omega>\{.*?\})',
                   re.DOTALL)

    knowledge_skills_expression = \
        re.compile(r'\\kskill(?P<name>\{.*?\})(?P<level1>\{.*?\})' +
                   r'(?P<level2>\{.*?\})(?P<level3>\{.*?\})' +
                   r'(?P<level4>\{.*?\})(?P<level5>\{.*?\})' +
                   r'(?P<Further>\{.*?\})(?P<Greater>\{.*?\})' +
                   r'(?P<Omega>\{.*?\})', re.DOTALL)

    # set up the config parser
    config = configparser.ConfigParser(interpolation=None)

    # define some constants to help with looping

    for match in skills_expression.finditer(tex):
        name = match.group('name').strip('{}').replace('\n', ' ')
        config[name] = {}
        config[name]['is_knowledge'] = 'no'
        for skill in SKILL_OPTIONS:
            config[name][skill] = \
                match.group(skill).strip('{}').replace('\n', ' ')
    for match in knowledge_skills_expression.finditer(tex):
        name = match.group('name').strip('{}').replace('\n', ' ')
        config[name] = {}
        config[name]['is_knowledge'] = 'yes'
        for skill in KNOWLEDGE_SKILL_OPTIONS:
            config[name][skill] = \
                match.group(skill).strip('{}').replace('\n', ' ')
    config['SECTION_HEADERS'] = {}
    for match in section_experssion.finditer(tex):
        name = match.group('name').replace('\n', ' ')
        config['SECTION_HEADERS'][name] = \
            match.group('disc').replace('\n', ' ')

    return config

TREES = collections.OrderedDict([
    ('Attack', ['Close Combat', 'Long Range', 'Melee', 'Light Combat',
                'Overdrive', 'Dexterity', 'Precision',
                'Attack Improvisation']),
    ('Defense', ['Shield', 'Stealth', 'Perception', 'Immunity', 'Aura',
                 'Counter', 'Trap', 'Disarm']),
    ('Knowledge', ['Battle', 'Magic', 'Historic', 'Piloting',
                   'Technical', 'Naturalistic', 'Medical', 'Charisma']),
    ('Magic', ['Cast', 'Heal', 'Alchemy', 'Summon', 'Status', 'Mind',
               'Geomancy', 'Shape-Shifting']),
    ('Mechanics', ['AI', 'Engine', 'Infection', 'Extension', 'Drones',
                   'Transform', 'Fields']),
    ('Ancients', ['Dragon', 'Hydra', 'Ares', 'Dimension', 'Controlia', 'Hades',
                  'Titan', 'Centaur']),
    ('Drifting', ['Space', 'Time', 'Ancient', 'Dream', 'Dark', 'Arcane',
                  'Cyber', 'Kinetic']),
])


def ini_to_tex(ini):
    """
    Function that converts the ini format back to LaTeX

    input:
        str ini - ini to convert back to tex
    returns:
        str tex - tex to converted from ini
    """
    config = configparser.ConfigParser(interpolation=None)
    config.read_string(ini)
    tex = "\\chapter{Skills}\n"
    for tree in TREES:
        tex += ('\\section{{{}}}'+'\n'*2).format(tree)
        tex += config['SECTION_HEADERS'][tree] + '\n'*2
        for skill in TREES[tree]:
            if config[skill].getboolean('is_knowledge'):
                skill_text = (r'\kskill' + '{{{}}}'*9).format(
                    skill, config[skill]['level1'],
                    config[skill]['level2'], config[skill]['level3'],
                    config[skill]['level4'], config[skill]['level5'],
                    config[skill]['further'], config[skill]['greater'],
                    config[skill]['omega'])
            else:
                skill_text = (r'\skill'+'{{{}}}'*7).format(
                    skill, config[skill]['level1'],
                    config[skill]['level2'], config[skill]['level3'],
                    config[skill]['level4'], config[skill]['level5'],
                    config[skill]['omega'])
            tex += skill_text + '\n'*2
    return tex


def parse_args():
    parser = argparse.ArgumentParser(
        description="""A tool that converts the skills file to ini and tex and
        back""")
    parser.add_argument("to", choices=['tex', 'ini'], default='ini',
                        help="direction of conversion")
    parser.add_argument("infile", type=argparse.FileType('r'),
                        help="file to read in as input")
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                        default=sys.stdout, help="file to read in as input")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    infile = args.infile.read()
    if args.to == 'tex':
        args.outfile.write(ini_to_tex(infile))
    elif args.to == 'ini':
        config = tex_to_ini(infile)
        config.write(args.outfile)
