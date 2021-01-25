#!/usr/bin/python3

import argparse
import pathlib
import re
import yaml

# Copy paste the output of this script to
# https://www.open-scap.org/security-policies/choosing-policy/
# between
# <!-- INSERT THE GENERATED LIST HERE -->
# and <!-- END OF GENERATED LIST -->

def list_profiles(ssg_root):
    p = pathlib.Path(ssg_root)
    for product_file in p.glob("**/product.yml"):
        product_dir = product_file.parent
        product_id = product_dir.name
        if product_id in ["example", "test_playbook_builder_data"]:
            continue
        with open(product_file, "r") as f:
            pinfo = yaml.full_load(f)
        product_name = pinfo["full_name"]
        print(f'<h4>{product_name}</h4>')
        print(f'<ul>')
        profiles_dir = product_dir / "profiles"
        for profile_file in profiles_dir.glob("*.profile"):
            with open(profile_file, "r") as g:
                profile = yaml.full_load(g)
            documentation_complete = profile["documentation_complete"]
            if not documentation_complete:
                continue
            profile_id = profile_file.stem
            profile_title = profile["title"]
            print(f'<li><a class="light-link" href="http://static.open-scap.org/ssg-guides/ssg-{product_id}-guide-{profile_id}.html">{profile_title}</a></li>')
        print('</ul>')
        print('<div class="brSpace"></div>')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ssg_root")
    args = parser.parse_args()
    list_profiles(args.ssg_root)