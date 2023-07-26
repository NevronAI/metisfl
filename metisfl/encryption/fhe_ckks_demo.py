import numpy as np
import os

from metisfl import config
from metisfl.encryption.fhe import CKKS
from metisfl.utils.logger import MetisLogger


def encrypt(crypto_params_files, ckks_scheme, data):
    MetisLogger.info("Encrypting...")
    ckks_scheme.load_crypto_context_from_file(
        crypto_params_files["crypto_context_file"])
    ckks_scheme.load_public_key_from_file(
        crypto_params_files["public_key_file"])

    learners_data_encrypted = []
    for x in data:
        res_enc = ckks_scheme.encrypt(x)
        learners_data_encrypted.append(res_enc)
    MetisLogger.info("Encrypting is complete.")

    return learners_data_encrypted

def decrypt(crypto_params_files, ckks_scheme, data_enc, number_of_elems):
    # Make sure the input data is a list.
    if not isinstance(data_enc, list):
        data_enc = [data_enc]
    MetisLogger.info("Decrypting...")
    ckks_scheme.load_crypto_context_from_file(
        crypto_params_files["crypto_context_file"])
    ckks_scheme.load_private_key_from_file(
        crypto_params_files["private_key_file"])

    data_dec = []
    for x_enc in data_enc:
        res_dec = ckks_scheme.decrypt(x_enc, number_of_elems)
        # FIXME(hamzahsaleem): Why if the function call is not correct an encrypted message is generated?
        #  Just comment the line above and uncomment the one below to regenerate issue.
        # res_dec = ckks_scheme.decrypt(x_enc)
        data_dec.append(res_dec)
    MetisLogger.info("Decrypting is complete.")

    return data_dec

def aggregate(crypto_params_files, ckks_scheme, data_enc, scaling_factors):
    MetisLogger.info("Starting aggregation...")
    ckks_scheme.load_crypto_context_from_file(
        crypto_params_files["crypto_context_file"])
    agg_res = ckks_scheme.aggregate(
        data_enc, scaling_factors)
    MetisLogger.info("Aggregation is complete.")
    return agg_res

def test_ckks_api(batch_size, scaling_factor_bits, learners_data, scaling_factors, number_of_elems):
    MetisLogger.info("Generating crypto context and keys...")
    ckks_scheme = CKKS(batch_size, scaling_factor_bits)
    # Get crypto parameters filepaths.
    fctx, fpuk, fprk = config.get_crypto_resources()
    ckks_scheme.gen_crypto_params(fctx, fpuk, fprk)
    crypto_params = ckks_scheme.get_crypto_params()
    MetisLogger.info("Crypto parameters files:")
    for param, filename in crypto_params.items():
        MetisLogger.info("\t {}:{}".format(param, filename))

    ckks_scheme = CKKS(batch_size, scaling_factor_bits)
    learners_data_enc = encrypt(crypto_params, ckks_scheme, learners_data)

    ckks_scheme = CKKS(batch_size, scaling_factor_bits)
    learners_data_dec = decrypt(crypto_params, ckks_scheme, learners_data_enc, number_of_elems)
    MetisLogger.info("Learners Data Decrypted: {}".format(learners_data_dec))

    ckks_scheme = CKKS(batch_size, scaling_factor_bits)
    pwa_enc = aggregate(crypto_params, ckks_scheme, learners_data_enc, scaling_factors)

    ckks_scheme = CKKS(batch_size, scaling_factor_bits)
    pwa_dec = decrypt(crypto_params, ckks_scheme, pwa_enc, number_of_elems)
    MetisLogger.info("Aggregated (Decrypted) Result: {}".format(pwa_dec))

if __name__ == "__main__":
    """
    Through this demo we test the encryption, decryption and private weighted
    aggregation functions of the CKKS scheme. 
    
    To test each operation (encrypt, decrypt, pwa) in isolation and see which 
    crypto parameters are required to perform each operation, we create and 
    pass a separate CKKS scheme object at every function call. The corresponding 
    function loads the required crypto parameters through the given ckks scheme. 
    
    Specifically, for each operation we need the following crypto params: 
        encryption -> (crypto_context, public)
        decryption -> (crypto_context, private)
        pwa -> (crypto_context)     
    """

    # Define batch size and scaling factor bits of CKKS scheme.
    batch_size = 4096
    scaling_factor_bits = 52

    # Define demo example learners data and corresponding scaling factors.
    # In the first test case,
    number_of_learners = 2
    number_of_elems = 2 * batch_size
    learners_data = [[1 for _ in range(number_of_elems)]] * number_of_learners
    scaling_factors = [0.5] * number_of_learners
    # Just print the first 100 elements per learner.
    MetisLogger.info("Original learners data: {}".format([x[:100] for x in learners_data]))
    MetisLogger.info("Original scaling factors: {}".format(np.array(scaling_factors[:number_of_learners])))
    test_ckks_api(batch_size, scaling_factor_bits, learners_data, scaling_factors, number_of_elems)

    number_of_learners = 2
    number_of_elems = (2 * batch_size) + 1
    learners_data = [[2 for _ in range(number_of_elems)]] * number_of_learners
    scaling_factors = [0.5] * number_of_learners
    # Just print the first 100 elements per learner.
    MetisLogger.info("Original learners data: {}".format([x[:100] for x in learners_data]))
    MetisLogger.info("Original scaling factors: {}".format(np.array(scaling_factors[:number_of_learners])))
    test_ckks_api(batch_size, scaling_factor_bits, learners_data, scaling_factors, number_of_elems)