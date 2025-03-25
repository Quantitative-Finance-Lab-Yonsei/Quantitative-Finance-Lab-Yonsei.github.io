# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "Quantitative Finance Lab"
  spec.version       = "0.1.3"
  spec.authors       = ["Ahn Kwang-Won"]
  spec.email         = ["k.ahn@yonsei.ac.kr"]

  spec.summary       = "QUANTITATIVE FINANCE LAB."
  spec.homepage      = "https://github.com/Quantitative-Finance-Lab-Yonsei"
  spec.license       = "YONSEI UNIVERSITY"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README|_config\.yml)!i) }

  spec.add_runtime_dependency "jekyll", "~> 4.2.0"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.15.0"
  spec.add_runtime_dependency "jekyll-soopr-seo-tag", "~> 2.7.3"
  spec.add_runtime_dependency "rouge", "~> 3.23.0"
  spec.add_runtime_dependency "webrick", "~> 1.7"
end
