@test "renders file templates" {
  [[ $(python src/template.py --file=src/test/fixture/test_vars.yml src/test/fixture/render.in.yml) == "rendered: success" ]]
}

@test "renders directories of templates" {
  [[ $(python src/template.py --dir=src/test/fixture/template_dir src/test/fixture/render.in.yml) == "rendered: success" ]]
}

@test "overrides variables" {
  [[ $(python src/template.py --dir=src/test/fixture/template_dir --file=src/test/fixture/test_override.yml src/test/fixture/override.in.yml) == "override: success" ]]
}
