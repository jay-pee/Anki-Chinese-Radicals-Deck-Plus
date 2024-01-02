from add_examples_to_source import add_examples_to_source
from download_ancient_img import download_ancient_img
from generate_deck import generate_deck
from get_radicals_data import get_radicals_data
from make_ancient_img_url_list import make_ancient_img_url_list

MAKE_NEW_ANCIENT_IMG_LIST = False
REDOWNLOAD_ANCIENT_IMG = False

if __name__ == "__main__":
    if MAKE_NEW_ANCIENT_IMG_LIST:
        make_ancient_img_url_list()
    if REDOWNLOAD_ANCIENT_IMG:
        download_ancient_img()
    get_radicals_data()
    add_examples_to_source()
    generate_deck()
