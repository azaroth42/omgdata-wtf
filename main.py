
def define_env(env):
  "Hook function"

  @env.macro
  def bar():
      return """ `foo` """