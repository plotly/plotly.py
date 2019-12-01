
export PLOTLY_RENDERER=notebook_connected

MD_DIR ?= python
UNCONV_DIR ?= unconverted/python
IPYNB_DIR ?= build/ipynb
HTML_DIR ?= build/html
FAIL_DIR ?= build/failures
REDIR_DIR ?= build/html/redir

MD_FILES := $(shell ls $(MD_DIR)/*.md)
UNCONV_FILES := $(shell ls $(UNCONV_DIR)/*.md)

IPYNB_FILES := $(patsubst $(MD_DIR)/%.md,$(IPYNB_DIR)/%.ipynb,$(MD_FILES))
HTML_FILES := $(patsubst $(MD_DIR)/%.md,$(HTML_DIR)/2019-07-03-%.html,$(MD_FILES))
NEXT_REDIR_FILES := $(patsubst $(MD_DIR)/%.md,$(REDIR_DIR)/2019-07-03-redirect-next-%.html,$(MD_FILES))
V3_REDIR_FILES := $(patsubst $(UNCONV_DIR)/%.md,$(REDIR_DIR)/2019-07-03-redirect-v3-%.html,$(UNCONV_FILES))


all: $(HTML_FILES) $(V3_REDIR_FILES) $(NEXT_REDIR_FILES)

.PRECIOUS: $(IPYNB_FILES)

$(IPYNB_DIR)/.mapbox_token: $(MD_DIR)/.mapbox_token
	@mkdir -p $(IPYNB_DIR)
	cd $(IPYNB_DIR) && ln -s ../../$<

$(IPYNB_FILES): $(IPYNB_DIR)/.mapbox_token

$(IPYNB_DIR)/%.ipynb: $(MD_DIR)/%.md
	@mkdir -p $(IPYNB_DIR)
	@echo "[jupytext]   $<"
	@jupytext $< --to notebook --quiet --output $@

$(HTML_DIR)/2019-07-03-%.html: $(IPYNB_DIR)/%.ipynb
	@mkdir -p $(HTML_DIR)
	@mkdir -p $(FAIL_DIR)
	@echo "[nbconvert]  $<"
	@jupyter nbconvert $< --to html --template nb.tpl \
	  	--output-dir $(HTML_DIR) --output 2019-07-03-$*.html \
	  	--execute > $(FAIL_DIR)/$* 2>&1  && rm -f $(FAIL_DIR)/$*


$(REDIR_DIR)/2019-07-03-redirect-next-%.html: $(IPYNB_DIR)/%.ipynb
	@mkdir -p $(REDIR_DIR)
	@echo "[next-redir] $<"
	@jupyter nbconvert $< --to html --template next_redirect.tpl \
	  	--output-dir $(REDIR_DIR) --output 2019-07-03-redirect-next-$*.html


$(REDIR_DIR)/2019-07-03-redirect-v3-%.html: $(UNCONV_DIR)/%.md
	@mkdir -p $(REDIR_DIR)
	@echo "[v3-redir]   $<"
	@echo "---" > $(REDIR_DIR)/2019-07-03-redirect-v3-$*.html
	@echo "permalink: python/$*/" >> $(REDIR_DIR)/2019-07-03-redirect-v3-$*.html
	@echo "redirect_to: https://plot.ly/python/v3/$*/" >> $(REDIR_DIR)/2019-07-03-redirect-v3-$*.html
	@echo "sitemap: true" >> $(REDIR_DIR)/2019-07-03-redirect-v3-$*.html
	@echo "---" >> $(REDIR_DIR)/2019-07-03-redirect-v3-$*.html
