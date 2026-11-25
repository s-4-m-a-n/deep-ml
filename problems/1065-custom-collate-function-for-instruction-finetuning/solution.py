def custom_collate(batch, pad_token_id=50256, ignore_index=-100, allowed_max_length=None):
    # Your code here
    batch_max_length = max(len(item)+1 for item in batch)
    inputs = []
    targets = []
    for item in batch:
        pad_len = batch_max_length - len(item)
        padded = item + [pad_token_id]*pad_len
        input_ = padded[:-1]
        target_ = padded[1:]
                
        pad_idx = target_.index(pad_token_id)+1
        for i in range(pad_idx, len(target_)):
            target_[i] = ignore_index

        if allowed_max_length:
            input_ = input_[:allowed_max_length]
            target_ = target_[:allowed_max_length]
        inputs.append(input_)
        targets.append(target_)

    return {"inputs": inputs, "targets": targets}