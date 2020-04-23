import sys
from Snowball.Snowball import Snowball

def main():
    if len(sys.argv) != 7:
        print("\nSnowball.py paramters.cfg sentences_file seeds_file_positive seeds_file_negative similarity_threshold" \
              " confidance_threshold\n")
        sys.exit(0)
    else:
        configuration = sys.argv[1]
        sentences_file = sys.argv[2]
        seeds_file = sys.argv[3]
        negative_seeds = sys.argv[4]
        similarity = sys.argv[5]
        confidance = sys.argv[6]

        snowball = Snowball(configuration, seeds_file, negative_seeds, sentences_file, float(similarity), float(confidance))
        if sentences_file.endswith('.pkl'):
            snowball.init_bootstrapp(tuples=sentences_file)
        else:
            snowball.generate_tuples(sentences_file)
            snowball.init_bootstrapp(tuples=None)


if __name__ == "__main__":
    sentences_file = "data/sentences.txt"
    config_file = "parameters.cfg"

    seeds_file_pos = "data/seed_positive.txt"
    seeds_file_neg = "data/seed_negative.txt"

    sim_threshold = 0.7
    conf_threshold = 0.6

    snowball = Snowball(config_file, seeds_file_pos, seeds_file_neg, sentences_file,
                        float(sim_threshold), float(conf_threshold))
    if sentences_file.endswith('.pkl'):
        snowball.init_bootstrapp(tuples=sentences_file)
    else:
        snowball.generate_tuples(sentences_file)
        snowball.init_bootstrapp(tuples=None)
