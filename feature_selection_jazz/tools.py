import numpy as np
import os

__author__ = 'Jakob Abesser'


def write_to_text_file(fn_txt, num, is_prob=False):
    if is_prob:
        content = generate_p_value_string(num)
    else:
        content = str(num)

    with open(fn_txt, 'w+') as f:
        f.write(content)


def generate_p_value_string(p):
    if p < 0.001:
        return '***'
    elif p < 0.01:
        return '**'
    elif p < 0.05:
        return '*'
    else:
        return 'n. s.'


def get_relative_position_in_phrase(phrase_id):
    """ Based on order of notes in the same phrase, this function derives a relative
        position of each note in its phrase
    Args:
        phrase_id (ndarray): Note-wise phrase ID values
    Returns:
        rel_pos_in_phrase (ndarray): Note-wise relative position within corresponding phrase
    """
    num_notes = len(phrase_id)
    unique_phrase_id = np.unique(phrase_id)
    num_phrases = len(unique_phrase_id)

    # initialize
    num_notes_per_phrase_id = np.zeros(num_phrases, dtype=float)
    note_count_per_phrase = np.zeros(num_phrases, dtype=float)
    rel_pos_in_phrase = np.zeros(num_notes, dtype=float)

    # get number of notes in each phrase
    for pid, curr_phrase_id in enumerate(unique_phrase_id):
        num_notes_per_phrase_id[pid] = np.sum(phrase_id == curr_phrase_id)

    # compute relative in-phrase-position for each note (0 - first note, 1 - last note)
    for nid, curr_phrase_id in enumerate(phrase_id):
        curr_phrase_num = np.where(unique_phrase_id == curr_phrase_id)[0][0]
        if num_notes_per_phrase_id[curr_phrase_num] > 1:
            rel_pos_in_phrase[nid] = note_count_per_phrase[curr_phrase_num] / (num_notes_per_phrase_id[curr_phrase_num] - 1)
        else:
            rel_pos_in_phrase[nid] = 0
        note_count_per_phrase[curr_phrase_num] += 1.

    return rel_pos_in_phrase


def cohens_d(x, y):
    """ Measure Cohen's d, which is an effect size measure for paired t-test
       -> 0.2 (small), 0.5 (medium), 0.8 (large)
       Use pooled variance to deal with unequal population sizes
    References:
        [1] https://en.wikipedia.org/wiki/Pooled_variance
        [2] http://trendingsideways.com/index.php/cohens-d-formula/
    """
    nx, ny = len(x), len(y)
    pooled_variance = ((nx - 1) * np.std(x, ddof=1) ** 2 +
                       (ny - 1) * np.std(y, ddof=1) ** 2) / \
                      ((nx - 1) + (ny - 1))
    return (np.mean(x) - np.mean(y)) / np.sqrt(pooled_variance)




