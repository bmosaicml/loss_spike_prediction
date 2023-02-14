


KEY_PREFIX = [
    'l2_norm/update',
    'l2_norm/grad/global',
    'l2_norm/grad/model',
    'l2_norm/param',
    'l2_norm/moment',
    'l2_norm/second_moment_sqrt',
    'l2_norm_ratio/moment_grad',
    'l2_norm_ratio/update_param',
    'cosine/moment_grad',
    'cosine/update_grad',
    'loss/train/total',
    'trainer/batch_idx'
]

RUNS = [
    {
        "m_params": 760, "wandb_url": "mosaic-ml/jeremy-gpt3-760m/vzmrapwg", "mcli_name": "gpt-760m-baseline-qmJfdR"
    },
    {
        "m_params": 760, "wandb_url": "mosaic-ml/jeremy-gpt3-760m/1bj8yavy", "mcli_name": "branching-gpt-760m-YrxVTk"
    },
    {
        "m_params": 760, "wandb_url": "mosaic-ml/jeremy-gpt3-760m/6wilzf64", "mcli_name": "gpt-760m-weight-tying-LczKSX"
    },
    {
        "m_params": 760, "wandb_url": "mosaic-ml/jeremy-gpt3-760m/10yhhbjf", "mcli_name": "gpt-760m-baseline",
    },
    {
        "m_params": 1315, "wandb_url": "mosaic-ml/jeremy-loss-spikes/ogjmpakr", "mcli_name": "gpt-1b-baseline-optimizer-monitor-ToI9ex",
    },
    {
        "m_params": 1315, "wandb_url": "mosaic-ml/jeremy-loss-spikes/1pwk36te", "mcli_name": "gpt-1b-baseline-egs0-1-0Y0ODb",
    },
    {
        "m_params": 2650, "wandb_url": "mosaic-ml/jeremy-loss-spikes/2e116nqm", "mcli_name": "gpt-3b-baseline-fScZNa",
    },
    {
        "m_params": 350, "wandb_url": "mosaic-ml/jeremy-loss-spikes/2g8cjo8t", "mcli_name": "gpt-350m-baseline-zLmNQJ",
    },
    {
        "m_params": 6658, "wandb_url": "mosaic-ml/jeremy-loss-spikes/2c58hv15", "mcli_name": "gpt-7b-egs-0-1-4KeMve",
    },
    {
        "m_params": 125, "wandb_url": "mosaic-ml/jeremy-loss-spikes/20vg3ygd", "mcli_name": "gpt-125m-baseline-0IsGnQ",
    },
    {
        "m_params": 350, "wandb_url": "mosaic-ml/jeremy-loss-spikes/2jbdv461", "mcli_name": "gpt-350m-egs-vg1ACI",
    },
    {
        "m_params": 125, "wandb_url": "mosaic-ml/jeremy-loss-spikes/3qiyr7jw", "mcli_name": "gpt-125m-lower-lr-FgBxJT",
    },
    {
        "m_params": 760, "wandb_url": "mosaic-ml/jeremy-loss-spikes/1yy3eubw", "mcli_name": "gpt-760m-baseline-wd1-5-gcnorm-0-5-ibVKXw",
    },
    {
        "m_params": 760, "wandb_url": "mosaic-ml/jeremy-loss-spikes/1u566rdr", "mcli_name": "gpt-760m-baseline-wd1-5-ZvlB9f",
    },
    {
        "m_params": 125, "wandb_url": "mosaic-ml/jeremy-loss-spikes/39iopve2", "mcli_name": "gpt-125m-wd1-5-gcnorm-0-5-W8uRk6",
    },
    {
        "m_params": 125, "wandb_url": "mosaic-ml/jeremy-loss-spikes/r0oua5to", "mcli_name": "gpt-125m-lr6e-4-JejH1w",
    },
    {
        "m_params": 350, "wandb_url": "mosaic-ml/jeremy-loss-spikes/13t6tsjs", "mcli_name": "gpt-350m-baseline-raise-lr-sU0C1z",
    },
    {
        "m_params": 1315, "wandb_url": "mosaic-ml/jeremy-loss-spikes/34ziuwos", "mcli_name": "gpt-1b-baseline-ycMJGh",
    },
    {
        "m_params": 1315, "wandb_url": "mosaic-ml/jeremy-loss-spikes/ev5uw22b", "mcli_name": "gpt-1b-baseline-2-Mc96yP",
    },
    {
        "m_params": 1315, "wandb_url": "mosaic-ml/jeremy-loss-spikes/15egfy2d", "mcli_name": "gpt-1b-baseline-2-dKLAKR",
    },
    {
        "m_params": 125, "wandb_url": "mosaic-ml/jeremy-loss-spikes/1mkq5mcx", "mcli_name": "gpt-125m-baseline-QmIdLi",
    },
    {
        "m_params": 1315, "wandb_url": "mosaic-ml/jeremy-loss-spikes/34kv6077", "mcli_name": "gpt-1b-baseline-numeric-logger-R8xyoj",
    },
    {
        "m_params": 760, "wandb_url": "mosaic-ml/jeremy-loss-spikes/38aqcqsj", "mcli_name": "pile-760m-amp_bf16-flash-s2048-par-fus-lnattn"
    },
    {
        "m_params": 760, "wandb_url": "mosaic-ml/jeremy-loss-spikes/3l2jl5cp", "mcli_name": "pile-760m-amp_bf16-flash-s2048-actckptFalse"
    },
    {
        "m_params": 6658, "wandb_url": "mosaic-ml/jeremy-loss-spikes/10jonalr", "mcli_name": "7b-amp_bf16-flash-s2048-actckptTrue-par-fus-lnattn"
    },
    {
        "m_params": 2650, "wandb_url": "mosaic-ml/jeremy-loss-spikes/2fqh8xq1", "mcli_name": "3b-amp_bf16-flash-s2048-actckptTrue-par-fus-lnattn"
    },
    {
        "m_params": 760, "wandb_url": "mosaic-ml/jeremy-loss-spikes/2idsckbe", "mcli_name": "760m-amp_bf16-flash-s2048-actckptTrue-par-fus-lnattn"
    },
]
