# -*- coding: utf-8 -*-
import configparser

legends = {
    'XXXXXXX': '',
    '_______': '',
    'KC_TRNS': '',
    'KC_NO': '',
    'LCTL(KC_Z)': 'UNDO',
    'LCTL(KC_Y)': 'REDO',
    'LCTL(KC_C)': 'COPY',
    'LCTL(KC_V)': 'PASTE',
    'LCTL(KC_X)': 'CUT',
    'KC_PSCREEN': 'PSc',
    'KC_GRV': '`',

    'MO(LOWER)': 'LOWER',
    'MO(RAISE)': 'RAISE',
    'RSFT_T(KC_ENT)': 'ET/SFT',
    'LALT(KC_TAB)': 'ALT-TAB',
    'LCTL(KC_G)': 'Ctrl-G',
    'LSFT(KC_SPACE)': 'Sft-SPC',

    'ESC_CTRL': 'ESC',
    'SSHOT': 'S/Shot',
    'OSL(MACRO)': 'MACRO',
    'TAB_TAP_HOLD': 'TAB',
    'SPC_NAV': 'Space',
    'FN_TAP_HOLD': 'Fn',

    'KC_MINS': '-',
    'KC_EQL': '=',
    'KC_LBRC': '[',
    'KC_RBRC': ']',
    'KC_PPLS': '+',
    'KC_PENT': 'ENTER',
    'KC_PDOT': '.',
    'KC_PSLS': '/',
    'KC_PAST': '*',
    'KC_PMNS': '-',
    'KC_SCLN': ';',
    'KC_QUOT': '\'',
    'KC_NUHS': '#',
    'KC_NUBS': '\\',
    'KC_COMM': ',',
    'KC_DOT': '.',
    'KC_SLSH': '/',

    'OSM(MOD_LSFT)': 'SHIFT',
    'OSM(MOD_RSFT)': 'SHIFT',
    'OSM(MOD_LGUI)': 'WIN',
    'OSM(MOD_RGUI)': 'WIN',
    'OSM(MOD_LALT)': 'ALT',
    'OSM(MOD_RALT)': 'ALT',
    'OSM(MOD_LCTL)': 'CTRL',
    'OSM(MOD_RCTL)': 'CTRL',
}

def read_config(config_file_path):
    if config_file_path:
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read_file(config_file_path)
        if 'legends' in config._sections:
            config_legends = config._sections.get("legends")
            legends.update(config_legends)
    return legends
